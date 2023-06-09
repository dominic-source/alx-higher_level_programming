#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a = tuple_a[0]
        c = tuple_a[1]
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        c = 0
    elif len(tuple_a) == 0:
        a = 0
        c = 0

    if len(tuple_b) >= 2:
        b = tuple_b[0]
        d = tuple_b[1]
    elif len(tuple_b) == 1:
        b = tuple_b[0]
        d = 0
    elif len(tuple_b) == 0:
        b = 0
        d = 0

    tuple_r = a + b, c + d
    return tuple_r


if __name__ == '__main__':
    add_tuple()
