import unittest
from appgen import appgen


class AppgenTestCase(unittest.TestCase):
    def test_validfilenames(self):
        self.assertEqual((True, []), appgen.validfilenames("file1.yaml"))

        self.assertEqual((True, []), appgen.validfilenames("file1.json",
                                                           "file2.yaml"))

        self.assertEqual((True, []), appgen.validfilenames("file1.json",
                                                           "file2.json",
                                                           "file3.json"))

        self.assertEqual((False, ["file2.txt"]),
                         appgen.validfilenames("file1.json",
                                               "file2.txt"))
