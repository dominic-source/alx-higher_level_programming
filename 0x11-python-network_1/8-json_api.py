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
    ndat = {'g': val}
    res = requests.post(url, data=ndat)
    try:
        data = res.json()
        print(data)
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    urlfetch()
