import unittest
from appgen import appgen
from appgen.parser import Parser


class DumpTestCase(unittest.TestCase):
    def test_dump_1(self):
        self.testthing = "hello"
        self.parser = Parser(self.testthing)
        self.assertEqual("hello", self.parser.getdump())
