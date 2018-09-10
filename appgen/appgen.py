import sys
import json


def main():
    args = sys.argv[1:]
    dump = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
    print('args:', args)
