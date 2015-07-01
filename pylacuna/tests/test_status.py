#!/usr/bin/env python
import os
import unittest
import pylacuna.core.status as status
from mock import patch, MagicMock, ANY, call

import ast

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins  # pylint:disable=import-error
else:
    import builtins  # pylint:disable=import-error

STATUS_DICT = ast.literal_eval('''
{u'build_queue_len': 4,
 u'build_queue_size': 9,
 u'building_count': 45,
 u'empire': {u'alignment': u'self',
  u'id': u'51819',
  u'is_isolationist': u'1',
  u'name': u'MikeTwo'},
 u'energy_capacity': u'21457',
 u'energy_hour': u'258',
 u'energy_stored': 12048,
 u'food_capacity': u'20743',
 u'food_hour': 781,
 u'food_stored': 596,
 u'happiness': 60224,
 u'happiness_hour': u'300',
 u'id': u'358099',
 u'image': u'p38-3',
 u'name': u'Cloraphorm III',
 u'needs_surface_refresh': u'0',
 u'neutral_entry': u'28 06 2015 18:05:05 +0000',
 u'num_incoming_ally': 0,
 u'num_incoming_enemy': u'0',
 u'num_incoming_own': u'0',
 u'orbit': u'3',
 u'ore': {u'anthracite': 1,
  u'bauxite': 1,
  u'beryl': 1,
  u'chalcopyrite': 1,
  u'chromite': 1,
  u'fluorite': 3000,
  u'galena': 1,
  u'goethite': 1,
  u'gold': 1,
  u'gypsum': 1,
  u'halite': 1,
  u'kerogen': 1,
  u'magnetite': 1,
  u'methane': 1,
  u'monazite': 1,
  u'rutile': 1,
  u'sulfur': 7000,
  u'trona': 1,
  u'uraninite': 1,
  u'zircon': 1},
 u'ore_capacity': u'28150',
 u'ore_hour': 562,
 u'ore_stored': 19595,
 u'plots_available': u'0',
 u'population': 2160000,
 u'propaganda_boost': u'0',
 u'size': u'45',
 u'star_id': u'49729',
 u'star_name': u'Ouss Siek',
 u'surface_version': u'224',
 u'type': u'habitable planet',
 u'waste_capacity': u'28380',
 u'waste_hour': u'286',
 u'waste_stored': 9084,
 u'water': 8000,
 u'water_capacity': u'24340',
 u'water_hour': u'592',
 u'water_stored': 10149,
 u'x': u'426',
 u'y': u'-256',
 u'zone': u'1|-1'}
''')


class testStatus(unittest.TestCase):
    # def setUp(self):
    #     # Patch out requests
    #     patcher = patch('pylacuna.session.requests')
    #     self.mock_requests = patcher.start()
    #     self.addCleanup(patcher.stop)

    #     # Patch out pickle
    #     patcher = patch('pylacuna.session.pickle')
    #     self.mock_pickle = patcher.start()
    #     self.addCleanup(patcher.stop)

    def tearDown(self):
        pass

    def test_init(self):
        s = status.Status(STATUS_DICT)

    def test_resource_calcs(self):
        s = status.Status(STATUS_DICT)
        print s.resource_calcs()


if __name__ == '__main__':
    unittest.main()
