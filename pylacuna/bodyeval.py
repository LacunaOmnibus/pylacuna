#!/usr/bin/env python

import core.status

class BodyEval(object):
    def __init__(self, body):
        '''
        body -- A body object on which to perform calcs
        '''
        self.body = body

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
        for bldg in self.body.buildings:
            print bldg

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
