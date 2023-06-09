#!/usr/bin/python3


def no_c(my_string):
    str = ''
    for i in my_string:
        if i not in 'cC':
            str = str + i
    return str


if __name__ == '__main__':
    no_c('')
