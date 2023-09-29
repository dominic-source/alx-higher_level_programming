#!/usr/bin/python3

"""This module will fetch a response from a server

"""

from urllib.request import urlopen
import sys


def urlfetch():
    url = sys.argv[1]
    with urlopen(url) as response:
        obj = response.headers['X-Request-Id']
        print(obj)


if __name__ == '__main__':
    urlfetch()
