#!/usr/bin/python3
from sys import argv

i, res = 1, 0
if __name__ == '__main__':
    while i < len(argv):
        res += int(argv[i])
        i += 1
    print(res)
