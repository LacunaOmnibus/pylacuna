#!/usr/bin/env python
import requests
import pickle
import urlparse
from collections import defaultdict

import pylacuna.globals as g
import pylacuna.core.status as status


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
        url = urlparse.urljoin(server_uri, '/empire')
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return cls(server_uri, response.json(), save)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            cls = pickle.load(f)
            print "Getting session from file..."
            return cls

    @classmethod
    def create_or_load(cls, file_path, server_uri, username, password,
                       save=True):
        ''' A convenience function for loading a session if it is available and
        creating it otherwise.
        '''
        _tmp = None
        try:
            _tmp = cls.load(g.SESSION_FILE)

        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        # Check if active.
        if _tmp is not None and not _tmp.is_active():
            _tmp.logout()
            _tmp = None

        # New login ()
        if _tmp is None:
            _tmp = cls.login(server_uri, username, password, save)

        if _tmp.is_active():
            return _tmp
        else:
            raise RuntimeError('Could not create active session')

    def logout(self):
        print "Logging out {}".format(self.id)
        return self.call_method_with_session_id('empire', 'logout', [self.id])

    def save(self, filename):
        ''' Saves itself to a file '''
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    def _prep_payload(self, method, params):
        payload = {
            "id": self.request_id,
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        self.request_id += 1
        return payload

    def call_method_with_session_id(self, route, method, params=None):
        '''
        POSTs a JSON RPC 2.0 method to server/route/

        The workhorse of this class. This method is used by almost every
        core driver to make calls to the API. It will automatically prepend
        the session ID to any other parameters.

        route -- The section of url to append to the server. Examples are
                '/empire', '/stats', '/map'
        method -- The method to call at the specified route. Examples are
                'build', 'upgrade'
        params -- A list of parameters to supply to the method. Examples are
                x and y coordinates for a build. [3,-1]
        '''
        if params is None:
            params = []

        # Add session id as first parameter
        params.insert(0, self.id)
        payload = self._prep_payload(method, params)
        url = urlparse.urljoin(self.server, route)
        response = requests.post(url, json=payload)
        # Not sure if I should raise here or not....
        # response.raise_for_status()
        # ------------------------------------------
        data = response.json()
        if 'result' in data and 'status' in data['result']:
            self.status.update(data['result']['status'])
            print "Status updated. RPC calls: {}".format(self.status['empire']['rpc_count'])
        return response.json()

    def is_active(self):
        ''' Checks that a session is active by pinging the server for stats
        '''
        # print "Checking if session is active."
        result = self.call_method_with_session_id('stats', 'empire_rank', [])
        if 'error' in result:
            return False
        else:
            return True
