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

    def test_run(self):
        class Args():
            def __init__(self, devconffile, opsconffile, defaultsfile,
                         outputfile):
                self.devconffile = devconffile
                self.opsconffile = opsconffile
                self.defaultsfile = defaultsfile
                self.outputfile = outputfile

        testargs = Args('test/testinput/testcase1/devconf.json',
                        'test/testinput/testcase1/opsconf.json',
                        'test/testinput/testcase1/defaults.json',
                        None)
        expect = open('test/testinput/testcase1/application.json').read()
        self.assertEqual(expect, appgen.run(testargs))
        testargs = Args('test/testinput/testcase2/devconf.json',
                        'test/testinput/testcase2/opsconf.json',
                        'test/testinput/testcase2/defaults.json',
                        None)
        expect = open('test/testinput/testcase2/application.json').read()
        self.assertEqual(expect, appgen.run(testargs))
