#!/usr/bin/python3

"""This module will fetch a response from a server

"""

from urllib.request import urlopen


def urlfetch():
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        obj = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(obj)))
        print('\t- content: {}'.format(obj))
        print('\t- utf8 content: {}'.format(obj.decode('utf-8')))


if __name__ == '__main__':
    urlfetch()
