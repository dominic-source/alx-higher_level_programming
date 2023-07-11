#!/usr/bin/python3

"""Module that uses a function to write to a json file

"""

import json


def save_to_json_file(my_obj, filename):
    """save json object in filename"""

    with open(filename, mode='w', encoding='utf-8') as f:
        text = json.dumps(my_obj)
        f.write(text)
