#!/usr/bin/env python

import pylacuna.core.building as building
import redis_cache


class CacheableBuilding(building.Building):
    def __init__(self, cache, session, building_id, *args, **kwargs):
        # Create if necessary
        self.cache = cache
        try:
            cache.get('')
        except redis_cache.CacheMissException:
            pass

        super(Building, self).__init__(session, building_id, *args, **kwargs)
        self.session = session
        self.update(aDict)
        self.id = building_id
        if extended:  # Download full information if extended is asked
            self.view()
