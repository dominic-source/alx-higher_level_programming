#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print('{}: {}'.format(i, a_dictionary[i]))


if __name__ == '__main__':
    print_sorted_dictionary({})
