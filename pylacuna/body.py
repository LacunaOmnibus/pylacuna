

class Body(object):
    def __init__(self, session, body_id):
        '''
        session -- a Session object
        body_id -- the id for the body (planet or star?) to
        '''
        self.session = session
        self.buildings = self.get_buildings(body_id)

    def get_status(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_status',
            params=[body_id])

    def get_buildings(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildings',
            params=[body_id])

    def repair_list(self, body_id, building_ids):
        return self.session.call_method_with_session_id(
            route='body',
            method='repair_list',
            params=[body_id],
            building_ids=building_ids)

    def rearrange_buildings(self, body_id, arrangement):
        return self.session.call_method_with_session_id(
            route='body',
            method='rearrange_buildings',
            params=[body_id],
            arrangement=arrangement)

    def get_buildable(self, body_id, x, y, tag):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildable',
            params=[body_id],
            x=x, y=y, tag=tag)

    def rename(self, body_id, name):
        return self.session.call_method_with_session_id(
            route='body',
            method='rename',
            params=[body_id],
            name=name)

    def abandon(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='abandon',
            params=[body_id])

    def view_laws(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='view_laws',
            params=[body_id])

