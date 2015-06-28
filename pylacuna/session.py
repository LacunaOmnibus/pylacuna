#!/usr/bin/env python
import requests
import pickle

from ipdb import set_trace
from IPython import embed

import globals as g
import status

class Session(object):
    ''' Represents a logged-in session to Lacuna

        Has methods for logging in and out, and making arbitrary calls to the
        api

        Several ways to create a session:
        Session.login(server_uri, username, password)
        Session.load(file_path)

        Convenience constructor:
        Session.create_or_load(file_path, server_uri, username, password)

        Please note that the session will be pickled and saved locally unless
        you pass save=False to the constructors
    '''
    def __init__(self, server, _session, save=True):
        self.request_id = 1
        self.server = server
        self._session = _session
        self.id = _session['result']['session_id']
        self.status = status.Status(_session['result']['status'])
        if save:
            self.save(g.SESSION_FILE)

    def __str__(self):
        return str(self._session)

    @classmethod
    def login(cls, server_uri, username, password, save=True):
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "login",
            "params": [username, password, g.APIKEY]
        }
        print "Logging in via server"
        response = requests.post(server_uri+'empire', json=payload)
        response.raise_for_status()
        return cls(server_uri, response.json(), save)

    def logout(self):
        print "Logging out {}".format(self.id)
        return self.call_method_with_session_id('empire', 'logout', [self.id])

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            cls = pickle.load(f)
            print "Getting session from file..."
            return cls

    @classmethod
    def create_or_load(cls, file_path, server_uri, username, password, save=True):
        _tmp = None
        try:
            _tmp = cls.load(g.SESSION_FILE)

        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        # Just clear it if its inactive
        if _tmp is not None and not _tmp.is_active():
            _tmp.logout()
            _tmp = None

        if _tmp is None:
            _tmp = cls.login(server_uri, username, password, save)

        if _tmp.is_active():
            return _tmp
        else:
            raise RuntimeError('Could not create active session')

    def save(self, filename):
        ''' Saves itself to a file '''
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    def call_method_with_session_id(self, route, method, params=None):
        '''
        POSTs a JSON RPC 2.0 method at server/route/
        '''
        if params is None:
            params = []

        # Add session id as first parameter
        params.insert(0, self.id)
        payload = {
            "id": self.request_id,
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        print "Posting:\n{}".format(payload)
        response = requests.post(self.server+route, json=payload)
        # Not sure if I should raise here or not....
        # response.raise_for_status()
        # ------------------------------------------
        self.request_id += 1
        return response.json()

    def is_active(self):
        ''' Checks that a session is active by pinging the server for
        stats
        '''
        print "Checking if session is active."
        result = self.call_method_with_session_id('stats', 'empire_rank', [])
        print result
        if 'error' in result:
            return False
        else:
            return True
