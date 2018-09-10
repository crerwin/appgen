import sys
import argparse
import json
import logging
from appgen.merger import Merger
from appgen.configparser import ConfigParser


def main():
    logger = getlogger(logging.DEBUG)
    app = {}
    args = sys.argv[1:]
    argresults = getparser(args)
    configparser = ConfigParser()
    merger = Merger()
    valid = validfilenames(argresults.devconffile, argresults.opsconffile,
                           argresults.defaultsfile)
    if valid[0]:
        devconf = configparser.loadfile(argresults.devconffile)
        opsconf = configparser.loadfile(argresults.opsconffile)
        defaults = configparser.loadfile(argresults.defaultsfile)
        logger.debug('devconf: ' + json.dumps(devconf))
        logger.debug('opsconf: ' + json.dumps(opsconf))
        logger.debug('defaults: ' + json.dumps(defaults))
        app = merger.mergeconfigs(devconf, opsconf, defaults)
        if argresults.outputfile is not None:
            writefile(argresults.outputfile, json.dumps(app))
            return 0
        else:
            return json.dumps(app)
    else:
        logger.error('invalid file name(s): ' + ' '.join(valid[1]))


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


def writefile(filename, output):
    file = open(filename, "w")
    file.write(output)
    file.close()


def getparser(args):
    parser = argparse.ArgumentParser(description='Application Generator')
    parser.add_argument('-devconf', action='store',
                        dest='devconffile', required=True,
                        help='REQUIRED: developer configuration file')
    parser.add_argument('-opsconf', action='store',
                        dest='opsconffile', required=True,
                        help='REQUIRED: operations configuration file')
    parser.add_argument('-defaults', action='store',
                        dest='defaultsfile', required=True,
                        help='REQUIRED: defaults configuration file')
    parser.add_argument('-out', action='store', dest='outputfile',
                        help='Optional: specify a file to output application' +
                        ' configuration to.  Will output to STDOUT if not ' +
                        'specified.')
    return parser.parse_args(args)


def getlogger(level):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
