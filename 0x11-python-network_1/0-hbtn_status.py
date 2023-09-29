#!/usr/bin/python3

"""This module will fetch a response from a server

"""

from urllib.request import urlopen


def urlfetch():
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        obj = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(obj)))
        print('    - content: {}'.format(obj))
        print('    - utf8 content: {}'.format(obj.decode('utf-8')))


if __name__ == '__main__':
    urlfetch()
