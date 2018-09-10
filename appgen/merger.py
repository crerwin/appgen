class Merger():
    def __init__(self):
        self.app = {}

    def checkforconflicts(self, firstdict, seconddict):
        # check for conflicting keys in two dictionaries
        conflict = False
        conflicting_key = None
        for key in firstdict:
            if key in seconddict:
                conflict = True
                conflicting_key = key
        return conflict, conflicting_key

    def mergeconfigs(self, devdict, opsdict, defaults):
        # return a mesosphere application configuration as a dict from 3 inputs
        app = {}
        if self.checkforconflicts(devdict, opsdict) == (False, None):
            if self.checkforconflicts(opsdict, defaults) == (False, None):
                app.update(defaults)
                app.update(opsdict)
                app.update(devdict)
        return app
