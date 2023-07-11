#!/usr/bin/python3

"""Module that uses a function to load from a json file

"""

import json


def load_from_json_file(filename):
    """save json object in filename"""

    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.read()
        return json.loads(text)
