class Merger():
    def __init__(self):
        self.app = {}

    def checkforconflicts(self, devdict, opsdict):
        conflict = False
        conflicting_key = None
        for key in devdict:
            if key in opsdict:
                conflict = True
                conflicting_key = key
        return conflict, conflicting_key

    def checkforcompliance(self, devdict, allowedkeys):
        # deprecated...probably
        compliant = True
        for key in devdict:
            if key not in allowedkeys:
                compliant = False
        return compliant
