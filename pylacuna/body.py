#!/usr/bin/env python

class Body(object):
    def __init__(self, session, body_id):
        '''
        session -- a Session object
        body_id -- the id for the body (planet or star?) to
        '''
        self.session = session
        self.id = body_id
        self.buildings = self.get_buildings(body_id)

    def get_status(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_status',
            params=[self.id])

    def get_buildings(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildings',
            params=[self.id])

    def repair_list(self, building_ids):
        return self.session.call_method_with_session_id(
            route='body',
            method='repair_list',
            params=[self.id, building_ids])

    def rearrange_buildings(self, arrangement):
        return self.session.call_method_with_session_id(
            route='body',
            method='rearrange_buildings',
            params=[self.id, arrangement])

    def get_buildable(self, x, y, tag):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildable',
            params=[self.id, x, y, tag])

    def rename(self, name):
        return self.session.call_method_with_session_id(
            route='body',
            method='rename',
            params=[self.id, name])

    def abandon(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='abandon',
            params=[self.id])

    def view_laws(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='view_laws',
            params=[self.id])

    def build (self, building_name, x, y ):
        return self.session.call_method_with_session_id(
            route='buildings/{}'.format(building_name),
            method='build',
            params=[self.id, x, y])
