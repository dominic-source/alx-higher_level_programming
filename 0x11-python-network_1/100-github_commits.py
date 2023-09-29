#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests
import sys


def urlfetch():
    REPO = sys.argv[1]
    OWNER = sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json'}
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/commits?per_page=10'
    res = requests.get(url, headers=headers)
    for data in res.json():
        print('{}: {}'.format(data.get('sha'),
                              data.get('commit').get('author').get('name')))


if __name__ == '__main__':
    urlfetch()
