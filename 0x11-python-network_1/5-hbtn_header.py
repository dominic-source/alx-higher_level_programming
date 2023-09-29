#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    url = sys.argv[1]
    res = requests.get(url)
    obj = res.headers['X-Request-Id']
    print(obj)


if __name__ == '__main__':
    urlfetch()
