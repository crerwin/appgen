import unittest
from appgen.merger import Merger


class MergerTestCase(unittest.TestCase):
    def setUp(self):
        self.testmerger = Merger()

    def test_checkforconflicts(self):
        self.assertEqual(False,
                         self.testmerger.checkforconflicts({'a': 1, 'b': 2},
                                                           {'c': 3, 'd': 4}))
        self.assertEqual(True,
                         self.testmerger.checkforconflicts({'a': 1, 'b': 2},
                                                           {'b': 3, 'c': 4}))

    def test_checkforcompliance(self):
        self.assertEqual(True,
                         self.testmerger.checkforcompliance({'a': 1, 'b': 2},
                                                            ['a', 'b']))

        self.assertEqual(False,
                         self.testmerger.checkforcompliance({'a': 1, 'c': 2},
                                                            ['a', 'b']))

    def test_mergedicts(self):
        self.assertEqual({'a': 1, 'b': 2, 'c': 3, 'd': 4},
                         self.testmerger.mergedicts({'a': 1, 'b': 2},
                                                    {'c': 3, 'd': 4}))
        self.assertEqual({},
                         self.testmerger.mergedicts({'a': 1, 'b': 2},
                                                    {'b': 3, 'c': 4}))
