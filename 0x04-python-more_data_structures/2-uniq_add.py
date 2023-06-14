#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum_me = 0
    for i in set(my_list):
        sum_me += i
    return sum_me


if __name__ == '__main__':
    uniq_add()
