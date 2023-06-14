#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleteme = []
    for i, v in a_dictionary.items():
        if (v == value):
            deleteme.append(i)
    for m in deleteme:
        del a_dictionary[m]

    return a_dictionary


if __name__ == '__main__':
    complex_delete({}, 0)
