#!/usr/bin/python3

"""Module that reads stdin line by line and computes metrics


"""
import sys


def my_main():
    """The function that will solve the problem"""

    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            line_split = line.split()
            file_size = int(line_split[-1])
            status_code = line_split[-2]

            status[status_code] += 1
            size += file_size
            count += 1
            if count % 10 == 0:
                print("File size: {:d}".format(size))
                for k, v in sorted(status.items()):
                    if v > 0:
                        print("{}: {:d}".format(k, v))
    except KeyboardInterrupt:
        print("File size: {:d}".format(size))
        for k, v in sorted(status.items()):
            if v > 0:
                print("{}: {:d}".format(k, v), end='')


my_main()
