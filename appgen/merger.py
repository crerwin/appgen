class Merger():
    def __init__(self):
        self.app = {}

    def checkforconflicts(self, devdict, opsdict):
        conflict = False
        for key in devdict:
            if key in opsdict:
                conflict = True
        return conflict

    def checkforcompliance(self, devdict, allowedkeys):
        compliant = True
        for key in devdict:
            if key not in allowedkeys:
                compliant = False
        return compliant

    def mergedicts(self, devdict, opsdict):
        if not self.checkforconflicts(devdict, opsdict):
            return {**devdict, **opsdict}
        return {}
