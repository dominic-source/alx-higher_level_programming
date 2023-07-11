#!/usr/bin/python3

"""Module that will manipulate data using a function

"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def my_main():
    """my main function for the file handling"""

    my_list = []
    for i in range(1, len(sys.argv)):
        if i is not None:
            my_list.append(sys.argv[i])
    try:
        new_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        with open("add_item.json", mode='w', encoding='utf-8') as f:
            new_list = []
    finally:
        new_list = new_list + my_list[:]
        save_to_json_file(new_list, "add_item.json")


my_main()
