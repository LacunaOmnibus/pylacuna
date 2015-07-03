#!/usr/bin/env python

from redis_cache import SimpleCache, ExpiredKeyException, CacheMissException


class BodyEval(object):
    def __init__(self, body):
        '''
        body -- A body object on which to perform calcs
        '''
        self.body = body
        self.cache = SimpleCache(limit=100, expire=60*60*24)

    def __str__(self):
        desc = ("{name} ({id}) at <{x},{y}>\n"
                "Size {size} {type} in orbit {orbit} around {star_name} ({star_id})\n"
                "".format(**self.body))
        desc += "RESOURCES:\n" + self.get_resources()
        if self.is_owned():
            desc += "PRODUCTION:\n" + self.get_production()
        return desc

    def value(self):
        print self.body
        self.get_buildings()

        FOOD_FACTOR = 1.0
        WATER_FACTOR = 1.0
        ORE_FACTOR = 1.0
        ENERGY_FACTOR = 1.0
        HAPPINESS_FACTOR = 1.0
        OPEN_PLOTS_FACTOR = 1.0
        WASTE_FACTOR = 1.0
        OPEN_PLOTS_FACTOR = 1.0
        open_plots = int(self.body['plots_available']) - int(self.body['building_count'])
        CAPACITY_TARGET = 0.5
        resources = ['food', 'water', 'ore', 'energy', 'waste']
        cap_values = []
        return int(self.body['food_hour']) + int(self.body['water_hour']) + int(self.body['ore_hour']) + int(self.body['energy_hour']) + int(self.body['happiness_hour']) + open_plots - int(self.body['waste_hour'])

    def is_owned(self):
        return True if 'building_count' in self.body else False

    def get_production_buildings(self):
        self.get_buildings()
        prod = []
        for bldg in sorted(self.body.buildings, key=lambda bld: bld['name']):
            print bldg
            if (int(bldg["ore_hour"]) > 0 or
                    int(bldg["water_hour"]) > 0 or
                    int(bldg["food_hour"]) > 0 or
                    int(bldg["energy_hour"]) > 0):
                prod.append(bldg)
        return prod

    def get_buildings(self):
        for bldg in self.body.buildings:
            bldg = self.get_building_detail(bldg)
            print "{}".format(bldg)

    def find_seconds_to_bust_cache(self, building):
        ''' Given a building, find the soonest time when we would need to update
        from server, or returns None.
        Updates could be due to:
         - upgrade/downgrade
         - work being complete? (maybe)
        '''
        return None

    def get_building_detail(self, building):
        # See if we already have it
        if "energy_capacity" in building:
            self.cache.store(building.id, building, expire=self.find_seconds_to_bust_cache(building))
            return building

        # Try to get it from cache
        try:
            return self.cache.get(building.id)
        except (ExpiredKeyException, CacheMissException):
            # Ignore misses or expireds
            pass

        # Update from server
        building.view()
        self.cache.store(building.id, building, expire=self.find_seconds_to_bust_cache(building))
        return building

    def get_production(self):
        desc =  "  Water: {}/{} at {}/hr\n".format(self.body['water_stored'], self.body['water_capacity'], self.body['water_hour'])
        desc += "  Energy: {}/{} at {}/hr\n".format(self.body['energy_stored'], self.body['energy_capacity'], self.body['energy_hour'])
        desc += "  Food: {}/{} at {}/hr\n".format(self.body['food_stored'], self.body['food_capacity'], self.body['food_hour'])
        desc += "  Ore: {}/{} at {}/hr\n".format(self.body['ore_stored'], self.body['ore_capacity'], self.body['ore_hour'])
        desc += "  Waste: {}/{} at {}/hr\n".format(self.body['waste_stored'], self.body['waste_capacity'], self.body['waste_hour'])
        return desc

    def get_resources(self):
        return "  Water - {}\n{}".format(self.body['water'], self.get_ore_pretty())

    def get_ore_pretty(self):
        desc = ""
        for material in self.body['ore']:
            amount = int(self.body['ore'][material])
            if amount > 1:
                desc += "  {} - {}\n".format(material, amount)
        return desc
