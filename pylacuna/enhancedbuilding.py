#!/usr/bin/env python
from redis_cache import ExpiredKeyException, CacheMissException
import pylacuna.core.building as building
from caching import GLOBAL_CACHE


class EnhancedBuilding(building.Building):
    ''' A building with additional methods for AI calcs'''
    def __init__(self, *args, **kwargs):
        ''' Args are currently:
        session
        building_id
        aDict=None

        But check building.py for updates.
        '''
        self.cache = GLOBAL_CACHE
        super(EnhancedBuilding, self).__init__(*args, **kwargs)

    @classmethod
    def from_building(cls, bldg):
        return cls(bldg.session, bldg.id, bldg)

    def __sub__(self, other):
        return subtract_production(self, other)

    def subtract_production(self, other):
        ''' Returns the difference in production (SELF - OTHER) between itself and another
        building as a dictionary that looks like this:
        {
            "ore_hour": 0
            "water_hour": 0
            "food_hour": 0
            "energy_hour": 0
        }
        '''
        retval = {}
        retval["ore_hour"] = self["ore_hour"] - other['ore_hour']
        retval["water_hour"] = self["water_hour"] - other['water_hour']
        retval["food_hour"] = self["food_hour"] - other['food_hour']
        retval["energy_hour"] = self["energy_hour"] - other['energy_hour']
        return retval

    def view(self):
        key = "{}-{}".format(self.id, self['level'])
        # See if we already have it
        if "energy_capacity" in self:
            self.cache.store(key, self,
                             expire=self.find_seconds_to_bust_cache(self))
            return self

        # Try to get it from cache
        try:
            return self.cache.get(key)
        except (ExpiredKeyException, CacheMissException):
            # Ignore misses or expireds
            pass

        # Update from server
        super(EnhancedBuilding, self).view()
        self.cache.store(key, self, expire=self.find_seconds_to_bust_cache(self))
        return self

    def find_seconds_to_bust_cache(self, building):
        ''' Given a building, find the soonest time when we would need to update
        from server, or returns None (which uses the default expire time).
        Updates could be due to:
         - upgrade/downgrade
         - work being complete? (maybe)
        '''
        return None
