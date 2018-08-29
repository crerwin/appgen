import json
import yaml


class AppConfig():
    def __init__(self):
        self._id = ""
        self._cmd = ""
        self._cpus = 0.1
        self._mem = 10.0
        self._instances = 1

    def loadyaml(self, input):
        y = yaml.load(input)
        print(y)
        self._id = y['id']
        self._cmd = y['cmd']
        self._cpus = float(y['cpus'])
        self._mem = float(y['mem'])
        self._instances = int(y['instances'])

    def getjson(self):
        d = {
            "id": self._id,
            "cmd": self._cmd,
            "cpus": self._cpus,
            "mem": self._mem,
            "instances": self._instances
        }
        return json.dumps(d, indent=4)
