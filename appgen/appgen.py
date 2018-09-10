import sys
import json
from appgen.merger import Merger
from appgen.parser import Parser


def main():
    app = {}
    args = sys.argv[1:]
    parser = Parser()
    merger = Merger()
    if len(args) == 3:
        devconffile = args[0]
        opsconffile = args[1]
        defaultsfile = args[2]
        valid = validfilenames(devconffile, opsconffile, defaultsfile)
        if valid[0]:
            devconf = parser.loadfile(devconffile)
            opsconf = parser.loadfile(opsconffile)
            defaults = parser.loadfile(defaultsfile)
            app = merger.mergeconfigs(devconf, opsconf, defaults)
            return json.dumps(app)
        else:
            print("invalid file name(s): ", valid[1])
    else:
        print('appgen takes three arguments.  usage:'
              + 'appgen devconf.[yml|yaml|json] opsconf.[yml|yaml|json]'
              + ' defaults.[yml|yaml|json]')


def validfilenames(*filenames):
    valid = True
    invalidnames = []
    for filename in filenames:
        if not (filename.endswith('json') or
                filename.endswith('yaml') or
                filename.endswith('yml')):
                valid = False
                invalidnames.append(filename)
    return valid, invalidnames
