#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': f'Bearer {password}'}
    url = f'https://api.github.com/users/{username}'
    res = requests.get(url, headers=headers)
    print(res.json().get('id'))


if __name__ == '__main__':
    urlfetch()
