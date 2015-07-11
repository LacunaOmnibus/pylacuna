#!/usr/bin/env python
from functools import total_ordering


@total_ordering
class Building(dict):
    ''' Common methods for working with buildings '''
    def __init__(self, session, building_id, aDict=None):
        if aDict is None:
            aDict = {}
        super(Building, self).__init__()
        self.session = session
        if aDict is not None:
            self.update(aDict)
        self.id = building_id

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.id == other.id
        else:
            # Not sure if this is a good idea
            # Allows one to write:
            #   if (uid) in (list of buildings)
            return str(self.id) == str(other)

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        desc = "{name:25s} (lvl {level:2s}) at <{x:2s},{y:2s}>: {efficiency} efficiency".format(**self)
        if 'pending_build' in self and self['pending_build'] is not None:
            desc += "  UPGRADING: {} seconds left".format(self['pending_build']['seconds_remaining'])
        if 'work' in self and self['work'] is not None:
            desc += "  WORKING: {} seconds left".format(self['work']['seconds_remaining'])
        if 'upgrade' in self and self['upgrade'] is not None:
            desc += "  Can upgrade: {}".format(self['upgrade']['can'])
        if 'energy_capacity' in self:
            desc += "  (FULL DETAILS)"

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
        if 'building' not in data['result']:
            from ipdb import set_trace; set_trace()
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
