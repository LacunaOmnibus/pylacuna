

class Body(object):
    def __init__(self, session):
        self.session = session

    def get_status(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_status',
            body_id=body_id)

    def get_buildings(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildings',
            body_id=body_id)

    def repair_list(self, body_id, building_ids):
        return self.session.call_method_with_session_id(
            route='body',
            method='repair_list',
            body_id=body_id,
            building_ids=building_ids)

    def rearrange_buildings(self, body_id, arrangement):
        return self.session.call_method_with_session_id(
            route='body',
            method='rearrange_buildings',
            body_id=body_id,
            arrangement=arrangement)

    def get_buildable(self, body_id, x, y, tag):
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildable',
            body_id=body_id,
            x=x, y=y, tag=tag)

    def rename(self, body_id, name):
        return self.session.call_method_with_session_id(
            route='body',
            method='rename',
            body_id=body_id,
            name=name)

    def abandon(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='abandon',
            body_id=body_id)

    def view_laws(self, body_id):
        return self.session.call_method_with_session_id(
            route='body',
            method='view_laws',
            body_id=body_id)

