#!/usr/bin/env python

import os
import unittest
import pylacuna.session
from mock import patch


class testSession(unittest.TestCase):
    def setUp(self):
        # Patch out pickle and requests

        pass

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(1, 1)
        #  Examples:
        # self.assertEqual(fp.readline(), 'This is a test')
        # self.assertFalse(os.path.exists('a'))
        # self.assertTrue(os.path.exists('a'))
        # self.assertTrue('already a backup server' in c.stderr)
        # self.assertIn('fun', 'disfunctional')
        # self.assertNotIn('crazy', 'disfunctional')
        # with self.assertRaises(Exception):
        #   raise Exception('test')
        #
        # Unconditionally fail, for example in a try block that should raise
        # self.fail('Exception was not raised')


if __name__ == '__main__':
    unittest.main()
