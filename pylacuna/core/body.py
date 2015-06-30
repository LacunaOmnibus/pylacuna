#!/usr/bin/env python

import pylacuna.core.status as status
import pylacuna.core.building as building
import pylacuna.core.empire as empire

class Body(dict):
    def __init__(self, session, body_id):
        '''
        session -- a Session object
        body_id -- the id for the body (planet, space station, asteroid)
        '''
        super(Body, self).__init__()
        self.session = session
        self.id = body_id
        self.empire = empire.Empire({})
        self.buildings = self.get_buildings()

    # def __str__(self):
    #     desc = ("{name} ({id}) at <{x},{y}>\n"
    #             "Size {size} {type} in orbit {orbit} around {star_name} ({star_id})\n"
    #             "".format(**self))
    #     desc += "RESOURCES:\n" + self.get_resources()
    #     if self.is_owned():
    #         desc += "PRODUCTION:\n" + self.get_production()
    #     return desc

    def get_status(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_status',
            params=[self.id])

    def get_buildings(self):
        bldgs = self.session.call_method_with_session_id(
            route='body',
            method='get_buildings',
            params=[self.id])
        results = bldgs['result']
        if 'body' in results['status']:
            self.update(results['status']['body'])
        if 'empire' in results['status']:
            self.empire.update(results['status']['empire'])
        bldgs_list = []
        if 'buildings' in results:
            for x in results['buildings']:
                bldgs_list.append(building.Building(
                    session=self.session,
                    building_id=x,
                    aDict=results['buildings'][x]))
        return bldgs_list

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
