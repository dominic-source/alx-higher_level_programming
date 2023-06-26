#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    r = 0
    p = 0
    while p < x:
        try:
            print("{:d}".format(my_list[p]), end='')
            r += 1
        except IndexError:
            raise
        except Exception:
            pass
        p += 1
    print("")
    return r
