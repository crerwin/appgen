import json
import yaml


class AppConfig():
    def __init__(self):
        self._id = ""
        self._cmd = ""
        self._cpus = 0.1
        self._mem = 10.0
        self._instances = 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = str(value)

    @property
    def cpus(self):
        return self._cpus

    @cpus.setter
    def cpus(self, value):
        self._cpus = float(value)

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = str(value)

    @property
    def mem(self):
        return self._mem

    @mem.setter
    def mem(self, value):
        self._mem = float(value)

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        self._instances = int(value)

    def loadyaml(self, input):
        y = yaml.load(input)
        print(y)
        self.id = y['id']
        self.cmd = y['cmd']
        self.cpus = y['cpus']
        self.mem = float(y['mem'])
        self.instances = int(y['instances'])

    def getjson(self):
        d = {
            "id": self.id,
            "cmd": self.cmd,
            "cpus": self.cpus,
            "mem": self.mem,
            "instances": self.instances
        }
        return json.dumps(d, indent=4)
