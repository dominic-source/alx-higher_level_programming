#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for m in my_list:
        if m % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result


if __name__ == '__main__':
    divisible_by_2()
