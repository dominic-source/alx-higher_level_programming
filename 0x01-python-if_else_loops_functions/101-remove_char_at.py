#!/usr/bin/python3
def remove_char_at(str, n):
    store = ""
    for i in range(0, len(str)):
        if i != n:
            store += str[i]
    return(store)
