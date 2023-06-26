#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    r = 0
    try:
        while (r < x):
            print(my_list[r], end='')
            r += 1
    except IndexError:
        return r
    finally:
        print("")
    return r
