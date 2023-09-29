#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    urlfetch()
