#!/usr/bin/env python
import pylacuna.core.body
import pylacuna.core.star


class Map(dict):
    ''' Common methods for working with star maps'''
    def __init__(self, session, central_star_id=None):
        super(Map, self).__init__()
        self.session = session
        if central_star_id is None:
            home_planet_id = session.status['empire']['home_planet_id']
            home_planet = pylacuna.core.body.Body(session, home_planet_id)
            home_planet.get_status()
            central_star_id = home_planet['star_id']
        self.center = central_star_id
        self.stars = []

    def get_star_map(self, left, right, top, bottom):
        # http://us1.lacunaexpanse.com/api/Map.html#get_star_map
        assert left < right
        assert bottom < top
        return self.session.call_method_with_session_id(
            route='map',
            method='get_star_map',
            params=[left, right, top, bottom])

    def get_stars(self, x1, y1, x2, y2):
        assert abs(x1-x2) <= 30, "Requested area too big"
        assert abs(y1-y2) <= 30, "Requested area too big"
        return self.session.call_method_with_session_id(
            route='map',
            method='get_stars',
            params=[x1, y1, x2, y2])

    def check_star_for_incoming_probe(self, star_id):
        return self.session.call_method_with_session_id(
            route='map',
            method='check_star_for_incoming_probe',
            params=[star_id])

    def get_star(self, star_id):
        return self.session.call_method_with_session_id(
            route='map',
            method='get_star',
            params=[star_id])

    def get_star_by_name(self, name):
        return self.session.call_method_with_session_id(
            route='map',
            method='get_star_by_name',
            params=[name])

    def get_star_by_xy(self, x, y):
        return self.session.call_method_with_session_id(
            route='map',
            method='get_star_by_xy',
            params=[x, y])

    def search_stars(self, name):
        return self.session.call_method_with_session_id(
            route='map',
            method='search_stars',
            params=[name])

    def view_laws(self, star_id):
        return self.session.call_method_with_session_id(
            route='map',
            method='view_laws',
            params=[star_id])
