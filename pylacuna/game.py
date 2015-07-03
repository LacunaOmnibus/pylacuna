#!/usr/bin/env python

import requests
import json
import pickle
from datetime import datetime
from dateutil import tz, parser
import redis

# Pylacuna imports
import pylacuna.globals as g
import pylacuna.core.session as session
import pylacuna.core.user as user
import pylacuna.core.errors as errors
import pylacuna.core.body as body
import pylacuna.bodyeval as bodyeval


class Game(object):
    def __init__(self):
        print "Initializing:"
        self.server = self.get_server()
        self.resources = self.get_resources()
        self.user = self.create_or_load_user()
        self.session = session.Session.create_or_load(
            g.SESSION_FILE, self.server['uri'], **self.user)
        print "Game initialized."
        print "SESSION ID: {}".format(self.session.id)
        # self.home_planet = self.login_info['result']['status']['empire']['home_planet_id']

    def run(self):
        ''' Run the AI '''
        home = body.Body(self.session, self.session.status['empire']['home_planet_id'])
        be = bodyeval.BodyEval(home)
        print be
        from IPython import embed; embed()

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
                print "  --> resources from file"
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
        resources = requests.get(self.server['uri']+g.RESOURCES_FILE)
        resources.raise_for_status()
        with open(g.RESOURCES_FILE, 'w') as f:
            pickle.dump(resources, f)
        return resources

    def _resources_are_expired(self, resources):
        resource_expire_time = parser.parse(resources.headers['expires'])
        now = datetime.now(tz.tzlocal())
        print "Resources expire: {}".format(resource_expire_time)
        print "Current time:     {}".format(now)
        return resource_expire_time <= now

    def create_or_load_user(self):
        _tmp = None
        try:
            _tmp = user.User.load(g.USER_CONFIG)

        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        if _tmp is None:
            username = raw_input('Name:')
            password = raw_input('Password:')
            _tmp = user.User(username, password)

        return _tmp
