#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96:
            j = chr(ord(i) - 32)
        else:
            j = i
        print("{}".format(j), end='')
    print("")
