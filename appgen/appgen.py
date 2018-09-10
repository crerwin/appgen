import sys
import json
import logging
from appgen.merger import Merger
from appgen.configparser import ConfigParser


def main():
    logger = getlogger(logging.DEBUG)
    app = {}
    args = sys.argv[1:]
    configparser = ConfigParser()
    merger = Merger()
    if len(args) == 3:
        devconffile = args[0]
        opsconffile = args[1]
        defaultsfile = args[2]
        valid = validfilenames(devconffile, opsconffile, defaultsfile)
        if valid[0]:
            devconf = configparser.loadfile(devconffile)
            opsconf = configparser.loadfile(opsconffile)
            defaults = configparser.loadfile(defaultsfile)
            logger.debug('devconf:' + json.dumps(devconf))
            logger.debug('opsconf:' + json.dumps(opsconf))
            logger.debug('defaults: ' + json.dumps(defaults))
            app = merger.mergeconfigs(devconf, opsconf, defaults)
            return json.dumps(app)
        else:
            logger.error('invalid file name(s): ' + ' '.join(valid[1]))
    else:
        logger.error('appgen takes three arguments.  usage:'
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


def getlogger(level):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
