#!/usr/bin/env python
import pylacuna.core.building as building


class SpacePort(building.Building):
    '''
    API page: http://us1.lacunaexpanse.com/api/SpacePort.html
    '''
    def build_ship(self, ship_type, quantity=1):
        ''' type -- A ship type. Get from get_buildable. '''
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='XXXXXXXXXX',
            params=[self.id, ship_type, quantity])

    def view(self):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view',
            params=[self.id])

    def view_all_ships(self, paging, filter, sort):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view_all_ships',
            params=[self.id, paging, filter, sort])

    def view_foreign_ships(self, page_number):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view_foreign_ships',
            params=[self.id, page_number])

    def get_fleet_for(self, from_body_id, target):
        pass

    def get_ships_for(self, from_body_id, target):
        pass

    def send_ship(self, ship_id, target):
        pass

    def send_ship_types(self, from_body_id, target, types, arrival):
        pass

    def send_fleet(self, ship_ids, target, set_speed):
        pass

    def recall_ship(self, ship_id):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='recall_ship',
            params=[self.id, ship_id])

    def recall_all(self):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='recall_all',
            params=[self.id])

    def name_ship(self, ship_id, name):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='name_ship',
            params=[self.id,  ship_id, name])

    def scuttle_ship(self, ship_id):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='scuttle_ship',
            params=[self.id,  ship_id])

    def mass_scuttle_ship(self, ship_ids):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='mass_scuttle_ship',
            params=[self.id,  ship_ids])

    def view_ships_travelling(self, page_number):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view_ships_travelling',
            params=[self.id,  page_number])

    def view_ships_orbiting(self, page_number):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view_ships_orbiting',
            params=[self.id,  page_number])

    def prepare_send_spies(self, on_body_id, to_body_id):
        pass

    def send_spies(self, on_body_id, to_body_id, ship_id, spy_ids):
        pass

    def prepare_fetch_spies(self, on_body_id, to_body_id):
        pass

    def fetch_spies(self, on_body_id, to_body_id, ship_id, spy_ids):
        pass

    def view_battle_logs(self, building_id, page_number):
        return self.session.call_method_with_session_id(
            route='spaceport',
            method='view_battle_logs',
            params=[self.id, building_id, page_number])

