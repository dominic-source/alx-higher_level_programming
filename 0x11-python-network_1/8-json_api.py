#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    if len(sys.argv) < 2:
        val = ""
    else:
        val = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    ndat = {'q': val}
    res = requests.post(url, data=ndat)
    data = res.json()
    if res.raise_for_status() is not None:
        print('Not a valid JSON')
    else:
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')


if __name__ == '__main__':
    urlfetch()
