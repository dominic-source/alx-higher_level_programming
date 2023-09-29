#!/usr/bin/python3

"""This module will fetch a response from a server

"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


def urlfetch():
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urlencode(value).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    urlfetch()
