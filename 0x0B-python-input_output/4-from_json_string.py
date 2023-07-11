#!/usr/bin/python3

"""Module that makes understand json conversion

"""

import json


def from_json_string(my_str):
    """converrt json to string """

    return json.loads(my_str)
