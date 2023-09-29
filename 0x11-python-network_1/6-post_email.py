#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    res = requests.post(url, data)
    print(res.text)


if __name__ == '__main__':
    urlfetch()
