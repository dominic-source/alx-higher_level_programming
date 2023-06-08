#!/usr/bin/python3
import sys


def infinite():
    sum1 = 0
    count = len(sys.argv)
    if count > 1:
        for i in range(1, count):
            sum1 += int(sys.argv[i])
    print(sum1)


if __name__ == '__main__':
    infinite()
