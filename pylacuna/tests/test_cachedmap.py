#!/usr/bin/env python
import sys
import os
import unittest
from mock import patch, MagicMock, ANY, call

import pylacuna.cachedmap as cachedmap

import ast

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins  # pylint:disable=import-error
else:
    import builtins  # pylint:disable=import-error

def mock_api(route, method, params=None):
    if method == 'view':
        print "MOCK: Returning individual view"
        return None
    if method == 'get_buildings':
        print "MOCK: Returning get buildings response"
        return None
    print "MOCK: Returning mock"
    return MagicMock()


class testCachedMap(unittest.TestCase):
    def setUp(self):
        # Create session mock
        self.session_mock = MagicMock()
        self.session_mock.call_method_with_session_id.side_effect = mock_api

        # Creaet body mock
        self.mock_map = MagicMock()

        # Patch out stdout
        # use 'reload(sys)' in a test to undo
        # patcher = patch('sys.stdout')
        # patcher.start()
        # self.addCleanup(patcher.stop)

    def tearDown(self):
        pass

    def test_init_and_print(self):
        mymap = cachedmap.CachedMap(self.session_mock, self.mock_map)
        print self.mock_map.mock_calls
        print self.session_mock.mock_calls
        print mymap


if __name__ == '__main__':
    unittest.main()
