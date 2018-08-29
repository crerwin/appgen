from yaml import load, dump


class Parser():
    def __init__(self, thing):
        self.thing = thing

    def getdump(self):
        return self.thing

    def getinputsfromyaml(self, yaml):
        return 0

    def getappdefinition(self, inputs):
        return 0
