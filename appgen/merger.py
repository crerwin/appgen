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

    def mergeconfigs(self, devdict, opsdict, defaults):
        app = {}
        if self.checkforconflicts(devdict, opsdict) == (False, None):
            if self.checkforconflicts(opsdict, defaults) == (False, None):
                app.update(defaults)
                app.update(opsdict)
                app.update(devdict)
        return app
