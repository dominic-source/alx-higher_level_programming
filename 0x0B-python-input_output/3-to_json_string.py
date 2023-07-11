#!/usr/bin/python3

"""Module which implement the use of JSON

"""

import json


def to_json_string(my_obj):
    """serialize JSON format to string"""

    return json.dumps(my_obj)
