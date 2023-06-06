#!/usr/bin/python3
for i in range(0, 100):
    for n in range(i, 10):
        if i < n:
            if n > 1:
                print(",", end=' ')
            print("{}{}".format(i, n), end='')
print("")
