import unittest
from appgen.appconfig import AppConfig


class AppConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.default_json_output = '''{
    "id": "",
    "cmd": "",
    "cpus": 0.1,
    "mem": 10.0,
    "instances": 1
}'''

        self.json_output_1 = '''{
    "id": 1234,
    "cmd": "/bin/bash",
    "cpus": 0.1,
    "mem": 10.0,
    "instances": 1
}'''

        self.json_output_2 = '''{
    "id": 2345,
    "cmd": "/bin/sh",
    "cpus": 2.0,
    "mem": 1024.0,
    "instances": 3
}'''

        self.yaml_input_1 = '''
id: 1234
cmd: /bin/bash
cpus: 0.1
mem: 10.0
instances: 1'''

        self.yaml_input_2 = '''
id: 2345
cmd: /bin/sh
cpus: 2
mem: 1024.0
instances: 3'''

    def test_appconfig(self):
        testappconfig = AppConfig()
        self.assertEqual(self.default_json_output, testappconfig.getjson())

    def test_loadyaml(self):
        testappconfig = AppConfig()
        testappconfig.loadyaml(self.yaml_input_1)
        self.assertEqual(self.json_output_1, testappconfig.getjson())

    def test_loadyaml2(self):
        testappconfig = AppConfig()
        testappconfig.loadyaml(self.yaml_input_2)
        self.assertEqual(self.json_output_2, testappconfig.getjson())
