#!/usr/bin/env python
import pylacuna.enhancedbuilding as enhancedbuilding
# from pylacuna.core.body import Body
# from caching import GLOBAL_CACHE


class EnhancedBody(object):
    def __init__(self, body, cache):
        '''
        body -- A body object on which to perform calcs
        cache -- a cache object. Must support methods:
                get()
                store()
                keys()
        '''
        self.cache = cache
        self._body = body
        self.buildings = self.get_buildings()

    def __str__(self):
        try:
            desc = ("{name} ({id}) at <{x},{y}>\n"
                    "Size {size} {type} in orbit {orbit} around {star_name} ({star_id})\n"
                    "".format(**self._body))
            desc += "RESOURCES:\n" + self.get_resources()
            if self.is_owned():
                desc += "PRODUCTION:\n" + self.get_production()
        except KeyError:
            return str(self.__dict__)
        return desc

    def repair_list(self, building_ids):
        return self._body.repair_list(building_ids)

    def rearrange_buildings(self, arrangement):
        return self._body.rearrange_buildings(arrangement)

    def get_buildable(self, x, y, tag):
        return self._body.get_buildable(x, y, tag)

    def rename(self, name):
        return self._body.self(name)

    def abandon(self):
        return self._body.abandon()

    def view_laws(self):
        return self._body.view_laws()

    def build(self, building_name, x, y):
        return self._body.self(building_name, x, y)

    # --------------------------------------

    def value(self):
        print self
        self.get_buildings()

        FOOD_FACTOR = 1.0
        WATER_FACTOR = 1.0
        ORE_FACTOR = 1.0
        ENERGY_FACTOR = 1.0
        HAPPINESS_FACTOR = 1.0
        OPEN_PLOTS_FACTOR = 1.0
        WASTE_FACTOR = 1.0
        OPEN_PLOTS_FACTOR = 1.0
        open_plots = int(self['plots_available']) - int(self['building_count'])
        CAPACITY_TARGET = 0.5
        resources = ['food', 'water', 'ore', 'energy', 'waste']
        cap_values = []
        return int(self['food_hour']) + int(self['water_hour']) + int(self['ore_hour']) + int(self['energy_hour']) + int(self['happiness_hour']) + open_plots - int(self['waste_hour'])

    def is_owned(self):
        return True if 'building_count' in self else False

    def evaluate_upgrades(self, list_of_buildings):
        for bldg in list_of_buildings:
            if int(bldg['upgrade']['can']) != 1:
                print "Building {}({}) is not upgradeable".format(bldg['name'], bldg.id)
                continue
            tmp = bldg.get_stats_for_level(int(bldg['level']) + 1)
            buildingup = enhancedbuilding.EnhancedBuilding.from_building(tmp)
            buildingnow = enhancedbuilding.EnhancedBuilding.from_building(bldg)
            diff = buildingup - buildingnow
            print diff

    def get_production_buildings(self):
        print "CURRENT CACHE: {}\n{}".format(len(self.cache.keys()), self.cache.keys())
        self.get_buildings()
        prod = []
        for bldg in self.buildings:
            if "ore_hour" not in bldg:
                print "Skipping"
                continue
            if (int(bldg["ore_hour"]) > 0 or
                    int(bldg["water_hour"]) > 0 or
                    int(bldg["food_hour"]) > 0 or
                    int(bldg["energy_hour"]) > 0):
                print bldg
                prod.append(bldg)
        return prod

    def get_buildings(self):
        self.buildings = self._body.get_buildings()
        for bldg in self.buildings:
            bldg = enhancedbuilding.EnhancedBuilding(self.cache, bldg)
            bldg.view()
        return self.buildings

    def get_production(self):
        desc =  "  Water: {}/{} at {}/hr\n".format(self['water_stored'], self['water_capacity'], self['water_hour'])
        desc += "  Energy: {}/{} at {}/hr\n".format(self['energy_stored'], self['energy_capacity'], self['energy_hour'])
        desc += "  Food: {}/{} at {}/hr\n".format(self['food_stored'], self['food_capacity'], self['food_hour'])
        desc += "  Ore: {}/{} at {}/hr\n".format(self['ore_stored'], self['ore_capacity'], self['ore_hour'])
        desc += "  Waste: {}/{} at {}/hr\n".format(self['waste_stored'], self['waste_capacity'], self['waste_hour'])
        return desc

    def get_resources(self):
        return "  Water - {}\n{}".format(self['water'], self.get_ore_pretty())

    def get_ore_pretty(self):
        desc = ""
        for material in self['ore']:
            amount = int(self['ore'][material])
            if amount > 1:
                desc += "  {} - {}\n".format(material, amount)
        return desc
