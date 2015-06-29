#!/usr/bin/env python

class Status(dict):
    ''' Methods for updating/viewing statuses '''
    def __init__(self, status_dict):
        super(Status, self).__init__()
        self.update(status_dict)

    def resource_calcs(self):
        '''
        Testing some higher-level stuff
        Food, ore, water, energy, waste, happiness
        '''
        assert 'energy_capacity' in self
        resources = ['energy', 'water', 'ore', 'food', 'waste']
        stored = []
        rate = []
        capacity = []
        for resource in resources:
            stored.append((resource, int(self[resource+"_stored"])))
            rate.append((resource, int(self[resource+"_hour"])))
            capacity.append((resource, int(self[resource+"_capacity"])))
            print ("Resource: {}\n"
                   "  Current : {}\n"
                   "  /Hour   : {}\n"
                   "  Capacity: {}\n".format(resource,
                                             self[resource+"_stored"],
                                             self[resource+"_hour"],
                                             self[resource+"_capacity"]))
        min_stored = min(stored)
        print min_stored
        min_rate = min(rate)
        print min_rate
        min_capacity = min(capacity)
        print min_capacity
