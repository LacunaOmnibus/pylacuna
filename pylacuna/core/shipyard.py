#!/usr/bin/env python

import pylacuna.core.building as building


class Shipyard(building.Building):
    def view_build_queue(self, page_number=None):
        if page_number is None:
            page_number = []
        params = [self.id]
        params.extend(page_number)
        return self.session.call_method_with_session_id(
            route='buildings/shipyard',
            method='view_build_queue',
            params=params)

    def subsidize_build_queue(self):
        return self.session.call_method_with_session_id(
            route='buildings/shipyard',
            method='subsidize_build_queue',
            params=[self.id])

    def subsidize_ship(self, ship_id):
        return self.session.call_method_with_session_id(
            route='buildings/shipyard',
            method='subsidize_ship',
            params=[self.id, ship_id])

    def get_buildable(self, tag=None):
        ''' tag -- An optional tag to limit the list of available ships to something shorter. If no tag is specified, then all ships will be displayed.

        Trade
        Ships that can be used to carry resources between colonies.

        Colonization
        Ships used to get more planets.

        Intelligence
        Ships that deal with spies or intelligence gathering.

        Exploration
        Ships that allow the user to go out and explore the Expanse.

        War
        Ships that are used to attack or defend.

        Mining
        Ships that are used to gather resources from space.
        '''
        if tag is None:
            tag = []
        return self.session.call_method_with_session_id(
            route='buildings/shipyard',
            method='get_buildable',
            params=[self.id])

    def build_ship(self, ship_type, quantity=1):
        ''' type -- A ship type. Get from get_buildable. '''
        return self.session.call_method_with_session_id(
            route='buildings/shipyard',
            method='build_ship',
            params=[self.id, ship_type, quantity])


