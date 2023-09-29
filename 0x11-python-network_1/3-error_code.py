#!/usr/bin/python3

"""This module will fetch a response from a server

"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
import sys


def urlfetch():
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    urlfetch()
