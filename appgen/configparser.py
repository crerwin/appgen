import yaml
import json


class ConfigParser():
    def getdict(self, input, expected_format):
        if expected_format == 'json':
            dict = json.loads(input)
        elif expected_format == 'yaml':
            dict = yaml.load(input)
        else:
            dict = ""
        return dict

    def loadfile(self, filename):
        if filename.endswith('json'):
            input = open(filename).read()
            dict = self.getdict(input, 'json')
        elif filename.endswith('yml') or filename.endswith('yaml'):
            input = open(filename).read()
            dict = self.getdict(input, 'yaml')
        else:
            dict = ""
        return dict
