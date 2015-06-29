#!/usr/bin/env python

class Building(dict):
    ''' Common methods for working with buildings '''
    def __init__(self, session, building_id, aDict=None, extended=False):
        if aDict is None:
            aDict = {}
        super(Building, self).__init__()
        self.session = session
        self.update(aDict)
        self.id = building_id
        if extended:  # Download full information if extended is asked
            self.view()

    def __str__(self):
        desc = "{name:25s} (lvl {level:2s}) at <{x:2s},{y:2s}>: {efficiency} efficiency".format(**self)
        if 'pending_build' in self:
            desc += "  UPGRADING: {} seconds left".format(self['pending_build']['seconds_remaining'])
        if 'work' in self:
            desc += "  WORKING: {} seconds left".format(self['work']['seconds_remaining'])
        return desc

    def build(self, x, y):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='build',
            params=[self.id, x, y])

    def view(self):
        assert 'url' in self, "Must have a url to build"
        data = self.session.call_method_with_session_id(
            route=self['url'],
            method='view',
            params=[self.id])
        self.update(data['result']['building'])
        return data

    def upgrade(self):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='upgrade',
            params=[self.id])

    def demolish(self):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='demolish',
            params=[self.id])

    def downgrade(self):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='downgrade',
            params=[self.id])

    def get_stats_for_level(self, level):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='get_stats_for_level',
            params=[self.id, level])

    def repair(self):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route=self['url'],
            method='repair',
            params=[self.id])


