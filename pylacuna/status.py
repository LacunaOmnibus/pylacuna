#!/usr/bin/env python

class Status(dict):
    ''' Methods for updating/viewing status '''
    def __init__(self, status_dict):
        super(Status, self).__init__()
        self.update(status_dict)

    def test(self):
        print "A method"
