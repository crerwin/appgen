import json


def main():
    dump = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
    print(dump)
