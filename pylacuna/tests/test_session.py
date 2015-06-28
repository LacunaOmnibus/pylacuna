#!/usr/bin/env python

import os
import unittest
import pylacuna.session
from mock import patch, MagicMock, ANY, call

import ast

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins  # pylint:disable=import-error
else:
    import builtins  # pylint:disable=import-error


SESSION_EXPIRED_RESPONSE = '''
{u'error': {u'code': 1006,
  u'data': u'358099',
  u'message': u'Session expired.'},
 u'id': 1,
 u'jsonrpc': u'2.0'}
 '''

# This is the response from the server when a successful session is created
SESSION_DICT = ast.literal_eval('''
{u'id': 1,
 u'jsonrpc': u'2.0',
 u'result': {u'session_id': u'89f4403a-5474-4427-a432-cc6c475a5af5',
  u'status': {u'empire': {u'colonies': {u'358099': u'Cloraphorm III'},
    u'essentia': 1.1,
    u'has_new_messages': u'0',
    u'home_planet_id': u'358099',
    u'id': u'51819',
    u'insurrect_value': u'100000',
    u'is_isolationist': u'1',
    u'latest_message_id': u'0',
    u'name': u'MikeTwo',
    u'next_colony_cost': u'100000',
    u'next_colony_srcs': u'100000',
    u'next_station_cost': u'10000000000000000000',
    u'planets': {u'358099': u'Cloraphorm III'},
    u'primary_embassy_id': u'5048765',
    u'rpc_count': 193,
    u'self_destruct_active': u'0',
    u'self_destruct_date': u'08 06 2015 05:49:38 +0000',
    u'stations': {},
    u'status_message': u'Just getting started',
    u'tech_level': u'7'},
   u'server': {u'rpc_limit': 10000,
    u'star_map_size': {u'x': [-1500, 1500], u'y': [-1500, 1500]},
    u'time': u'28 06 2015 18:14:53 +0000',
    u'version': 3.0911}}}}
''')


class testStatus(unittest.TestCase):
    def setUp(self):
        # Patch out requests
        patcher = patch('pylacuna.session.requests')
        self.mock_requests = patcher.start()
        self.addCleanup(patcher.stop)

        # Patch out pickle
        patcher = patch('pylacuna.session.pickle')
        self.mock_pickle = patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(1, 1)



class testSession(unittest.TestCase):
    def setUp(self):
        # Patch out requests
        patcher = patch('pylacuna.session.requests')
        self.mock_requests = patcher.start()

        self.addCleanup(patcher.stop)

        # Patch out pickle
        patcher = patch('pylacuna.session.pickle')
        self.mock_pickle = patcher.start()
        self.addCleanup(patcher.stop)

        # Patch out file operations
        patcher = patch.object(builtins, 'open')
        patcher.return_value = MagicMock(spec=file)
        self.mock_open = patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        pass

    def test_basic_init(self):
        # Should not throw
        s = pylacuna.session.Session("testserver", SESSION_DICT)
        self.mock_open.assert_any_call('.session_info', 'w')

    def test_basic_init_no_save(self):
        s = pylacuna.session.Session("testserver", SESSION_DICT, save=False)
        self.assertFalse(self.mock_open.called)

    def test_init_from_file(self):
        s = pylacuna.session.Session.load('filename')

    def test_init_from_login(self):
        _tmp = MagicMock()
        self.mock_requests.post.return_value = _tmp
        _tmp.json.return_value = SESSION_DICT
        s = pylacuna.session.Session.login('http://nowhere.com/', 'username', 'password')
        self.mock_requests.post.assert_any_call('http://nowhere.com/empire', json=ANY)

    def test_generic_method_call(self):
        s = pylacuna.session.Session("http://testserver/", SESSION_DICT)
        expected = call(
            'http://testserver/route',
            json={
                'params': ['89f4403a-5474-4427-a432-cc6c475a5af5'],
                'jsonrpc': '2.0',
                'id': 1,
                'method': 'method'
            })
        ret = s.call_method_with_session_id('route', 'method', [])
        self.mock_requests.post.assert_has_calls([expected])


        # print self.mock_open.mock_calls
        # print self.mock_pickle.mock_calls





if __name__ == '__main__':
    unittest.main()
