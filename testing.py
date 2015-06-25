#!/usr/bin/env python
import requests
import json
import pickle
from datetime import datetime
from dateutil import tz, parser

from ipdb import set_trace
from IPython import embed

RESOURCES_FILE = 'resources.json'
SESSION_FILE = '.session_info'
USER_CONFIG = '.config'
API_KEY = "b66b76df-eb06-4ebd-b88d-c2ccb8a3d580"


def get_server():
    with open("servers.json", 'r') as f:
        text = f.read()
        servers = json.loads(text)
    main_server = servers[0]
    return main_server


def acquire_and_pickle(server):
    print "Getting resources from server"
    resources = requests.get(server['uri']+RESOURCES_FILE)
    resources.raise_for_status()
    with open(RESOURCES_FILE, 'w') as f:
        pickle.dump(resources, f)
    return resources


def resources_are_expired(resources):
    resource_expire_time = parser.parse(resources.headers['expires'])
    now = datetime.now(tz.tzlocal())
    print "Resources expire: {}".format(resource_expire_time)
    print "Current time:     {}".format(now)
    return resource_expire_time <= now


def get_resources(server):
    resources = None
    try:
        with open(RESOURCES_FILE, 'r') as f:
            resources = pickle.load(f)
            print "Getting resources from file"
    # Catch file no found errors
    except IOError as e:
        if not e.errno == 2:  # File not found
            raise

    if resources is None or resources_are_expired(resources):
        resources = acquire_and_pickle(server)

    assert resources is not None, "Resources should not be none"
    return resources


def login(server):
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "login",
        "params": ["MikeTwo", "NVGf=hh3", "b66b76df-eb06-4ebd-b88d-c2ccb8a3d580"]
    }
    response = requests.post(server['uri']+'empire', json=payload)
    return response, response.json()['result']['session_id']


class Game(object):
    def __init__(self):
        self.server = get_server()
        self.resources = get_resources(self.server)
        self.login_info = self.create_or_load_session()
        self.session_id = self.login_info['result']['session_id']
        print "SESSION ID: {}".format(self.session_id)
        self.home_planet = self.login_info['result']['status']['empire']['home_planet_id']

    def login(self):
        user = get_user_creds()
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "login",
            "params": [user['name'], user['password'], API_KEY]
        }
        print "Logging in via server"
        response = requests.post(self.server['uri']+'empire', json=payload)
        response.raise_for_status()
        with open(SESSION_FILE, 'w') as f:
            pickle.dump(response.json(), f)
        return response.json()

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
        if not self.session_active(session['result']['session_id']):
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


class BodyInfo(object):
    def __init__(self, gameobj, bodyid=None):
        self.server = gameobj.server
        self.session_id = gameobj.session_id
        if bodyid is None:
            self.body_id = gameobj.home_planet
        else:
            self.body_id = bodyid
        self.id = 1
        self.buildings = self.get_buildings()
        self.print_info()

    def get_buildings(self):
        payload = {
            "id": self.id,
            "jsonrpc": "2.0",
            "method": "get_buildings",
            "params": [self.session_id, self.body_id]
        }
        response = requests.post(self.server['uri']+'body', json=payload)
        self.id += 1
        return response.json()

    def print_info(self):
        lowest_level = None
        soonest_complete_upgrade = None
        soonest_complete_work = None
        for uid in self.buildings['result']['buildings']:
            building = self.buildings['result']['buildings'][uid]
            if "pending_build" in building:
                secs = building['pending_build']['seconds_remaining']
                if soonest_complete_upgrade is None or secs < soonest_complete_upgrade:
                    soonest_complete_upgrade = secs
            if "work" in building:
                secs = building['work']['seconds_remaining']
                if soonest_complete_work is None or secs < soonest_complete_work:
                    soonest_complete_work = secs
            if lowest_level is None or building['level'] < lowest_level:
                lowest_level = building['level']
        print lowest_level
        print soonest_complete_work
        print soonest_complete_upgrade


class Building(object):
    def __init__(self, build_dict):
        ''' build dict comes from the status contained in most responsess '''
        self.info = build_dict

    def __str__(self):
        return str(self.info)


def write_user_creds():
    name = raw_input('Name:')
    pw = raw_input('Password:')
    user = {
        'name': name,
        'password': pw
    }
    with open(USER_CONFIG, 'w') as f:
        pickle.dump(user, f)
    print "Wrote user credentials to file"
    return user


def get_user_creds():
    user = None
    try:
        with open(USER_CONFIG, 'r') as f:
            user = pickle.load(f)
            print "Getting user credentials from file"
    # Catch file no found errors
    except IOError as e:
        if not e.errno == 2:  # File not found
            raise

    if user is None:
        user = write_user_creds()

    return user


def main():
    gameobj = Game()
    body = BodyInfo(gameobj)

if __name__ == '__main__':
    main()

    # curl 'https://us1.lacunaexpanse.com/empire' -H 'Origin: https://us1.lacunaexpanse.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: */*' -H 'Referer: https://us1.lacunaexpanse.com/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data-binary '{"id":567,"method":"login","jsonrpc":"2.0","params":["MikeTwo","4%xR&Ie7E@ii5%w%LW","53137d8f-3544-4118-9001-b0acbec70b3d"]}' --compressed

# NVGf=hh3
