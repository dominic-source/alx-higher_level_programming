#!/usr/bin/python3
def islower(c):
    if c == "":
        raise ValueError
    elif c in 'abcdefghijklmnopqrstuvwxy':
        return True
    else:
        return False
