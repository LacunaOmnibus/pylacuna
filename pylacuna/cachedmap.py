#!/usr/bin/env python
from pylacuna.core.map import Map


class CachedMap(object):
    def __init__(self, aMap, cache):
        '''
        aMap -- A map object on which to perform calcs
        cache -- a cache object. Must support methods:
                get()
                store()
                keys()
        '''
        self.cache = cache
        self._map = aMap

    # def __str__(self):
    #     try:
    #         desc = ("{name} ({id}) at <{x},{y}>\n"
    #                 "Size {size} {type} in orbit {orbit} around {star_name} ({star_id})\n"
    #                 "".format(**self._body))
    #         desc += "RESOURCES:\n" + self.get_resources()
    #         if self.is_owned():
    #             desc += "PRODUCTION:\n" + self.get_production()
    #     except KeyError:
    #         return str(self.__dict__)
    #     return desc

    def get_star_map(self, **kwargs):
        return self._map.get_star_map(**kwargs)

    def get_stars(self, x1, y1, x2, y2):
        return self._map.get_stars(x1, y1, x2, y2)

    def check_star_for_incoming_probe(self, star_id):
        return self._map.check_star_for_incoming_probe(star_id)

    def get_star(self, star_id):
        return self._map.get_star(star_id)

    def get_star_by_name(self, name):
        return self._map.get_star_by_name(name)

    def get_star_by_xy(self, x, y):
        return self._map.get_star_by_xy(x, y)

    def search_stars(self, name):
        return self._map.search_stars(name)

    def view_laws(self, star_id):
        return self._map.view_laws(star_id)

    # ---------------------------------------------------------

    def get_home_map(self):
        x = self._map._center['x']
        y = self._map._center['y']
        # We need to get everything within an area of 1000 treating home as
        # center.
        xlow = int(x) - 15
        xhigh = int(x) + 15
        ylow = int(y) - 15
        yhigh = int(y) + 15
        retval = self._map.get_stars(xlow, yhigh, xhigh, ylow)
        return retval
