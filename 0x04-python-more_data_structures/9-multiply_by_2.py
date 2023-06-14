#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}
    for i, v in a_dictionary.items():
        result.update({i: (v * 2)})
    return result


if __name__ == '__main__':
    multiply_by_2({})
