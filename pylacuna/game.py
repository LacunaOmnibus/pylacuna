#!/usr/bin/env python

import requests
import json
import pickle
from datetime import datetime
from dateutil import tz, parser
import redis
import globals as g


class Game(object):
    def __init__(self):
        print "Initializing:"
        self.server = self.get_server()
        self.resources = self.get_resources()
        self.login_info = self.create_or_load_session()
        self.session_id = self.login_info['result']['session_id']
        print "SESSION ID: {}".format(self.session_id)
        self.home_planet = self.login_info['result']['status']['empire']['home_planet_id']

    def run(self):
        ''' Run the AI '''
        pass

    def get_server(self):
        print "Getting server..."
        with open("servers.json", 'r') as f:
            text = f.read()
            servers = json.loads(text)
        main_server = servers[0]
        return main_server

    def get_resources(self):
        print "Getting resources..."
        resources = None
        try:
            with open(g.RESOURCES_FILE, 'r') as f:
                resources = pickle.load(f)
                print "\t--> resources from file"
        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        if resources is None or self._resources_are_expired(resources):
            resources = self._acquire_and_pickle()

        assert resources is not None, "Resources should not be none"
        return resources

    def _acquire_and_pickle(self):
        print "Getting resources from server"
        resources = requests.get(server['uri']+g.RESOURCES_FILE)
        resources.raise_for_status()
        with open(g.RESOURCES_FILE, 'w') as f:
            pickle.dump(resources, f)
        return resources

    def _resources_are_expired(resources):
        resource_expire_time = parser.parse(resources.headers['expires'])
        now = datetime.now(tz.tzlocal())
        print "Resources expire: {}".format(resource_expire_time)
        print "Current time:     {}".format(now)
        return resource_expire_time <= now


    def session_active(self, session_id):
        ''' Checks that a session is active '''
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "empire_rank",
            "params": [session_id]
        }
        response = requests.post(self.server['uri']+'stats', json=payload)
        if response.status_code != 200:
            return False
        else:
            return True

    def create_or_load_session(self):
        session = None
        try:
            with open(SESSION_FILE, 'r') as f:
                session = pickle.load(f)
                print "Getting session from file"

        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        # Just clear it if its inactive
        if session is not None and not self.session_active(session['result']['session_id']):
            session = None

        if session is None:
            session = self.login()

        return session

    def acquire_and_pickle(server):
        print "STARTING NEW SESSION"
        resources = requests.get(server['uri']+RESOURCES_FILE)
        resources.raise_for_status()
        with open(RESOURCES_FILE, 'w') as f:
            pickle.dump(resources, f)
        return resources
