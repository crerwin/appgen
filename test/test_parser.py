import unittest
from appgen import appgen
from appgen.parser import Parser


class DumpTestCase(unittest.TestCase):
    def setUp(self):
        self.testparser = Parser()
        self.yaml_input_1 = '''
id: /jenkins
cmd: /bin/bash
cpus: 0.1
mem: 10.0
instances: 1'''

    def test_getdict(self):
        self.assertEqual({'a': 1, 'b': 2},
                         self.testparser.getdict('{"a": 1, "b": 2}', 'json'))

        self.assertEqual({'id': '/jenkins', 'cmd': '/bin/bash', 'cpus': 0.1,
                         'mem': 10.0, 'instances': 1},
                         self.testparser.getdict(self.yaml_input_1, 'yaml'))
