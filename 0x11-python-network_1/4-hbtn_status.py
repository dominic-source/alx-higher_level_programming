#!/usr/bin/python3

"""This module will fetch a response from a server

"""

import requests


def urlfetch():
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))


if __name__ == '__main__':
    urlfetch()
