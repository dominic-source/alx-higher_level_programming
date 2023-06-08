#!/usr/bin/python3
import sys


def arg_prt():
    count = len(sys.argv)
    if count == 1:
        print('0 arguments.')
    elif count == 2:
        print('1 argument:')
        print('1: {}'.format(sys.argv[1]))
    elif count > 2:
        print('{} arguments:'.format(count - 1))
        for i in range(1, count):
            print('{}: {}'.format(i, sys.argv[i]))


if __name__ == '__main__':
    arg_prt()
