import json
import yaml


class AppConfig():
    def __init__(self):
        self.id = ""
        self.cmd = ""
        self.cpus = 0.1
        self.mem = 10.0
        self.instances = 1

    def loadyaml(self, input):
        y = yaml.load(input)
        print(y)
        self.id = y['id']
        self.cmd = y['cmd']
        self.cpus = float(y['cpus'])
        self.mem = float(y['mem'])
        self.instances = int(y['instances'])

    def getjson(self):
        return json.dumps(self.__dict__, indent=4)
