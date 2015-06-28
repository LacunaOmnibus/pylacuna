#!/usr/bin/env python
import requests
import json
import pickle
from datetime import datetime
from dateutil import tz, parser

from ipdb import set_trace
from IPython import embed
import requests
import globals as g


class Session(object):
    ''' Represents a logged in session to Lacuna
        Has methods for logging in and out, and making calls to the api

        WAYS to create a session

        Session.login(server_uri, username, password)
        Session.load(file_path)
    '''
    def __init__(self, server, _session):
        self.server = server
        self._session = _session

    @classmethod
    def login(cls, server_uri, username, password):
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "login",
            "params": [username, password, g.APIKEY]
        }
        print "Logging in via server"
        response = requests.post(server_uri+'empire', json=payload)
        response.raise_for_status()
        return cls(server_uri, response.json())

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            cls = pickle.load(f)
            print "Getting session from file"
            return cls

    def save(self, filename):
        ''' Saves itself to a file '''
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    def call_method_with_session_id(self, route, method, params):
        '''
        POSTs a JSON RPC 2.0 method at server/route/
        '''
        payload = {
            "id": self.id,
            "jsonrpc": "2.0",
            "method": "get_buildings",
            "params": [self.session_id, self.body_id]
        }
        payload.update(kwargs)
        response = requests.post(self.server['uri']+'body', json=payload)
        self.id += 1
        return response.json()



