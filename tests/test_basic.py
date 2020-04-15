import unittest

import inject

from tests.bindings import test_config


class BasicTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        inject.clear_and_configure(test_config)
