import sys
import json
from appgen.parser import Parser


def main():
    args = sys.argv[1:]
    dump = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
    parser = Parser(dump)
    print('args:', args)
    print(parser.getdump())
