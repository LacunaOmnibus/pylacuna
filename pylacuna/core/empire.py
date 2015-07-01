#!/usr/bin/env python


class Empire(dict):
    ''' Methods for updating/viewing Empirees '''
    def __init__(self, Empire_dict):
        super(Empire, self).__init__()
        self.update(Empire_dict)
