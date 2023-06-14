#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_w = 0
    mult_w = 0
    for i, v in my_list:
        mult_w += i * v
        sum_w += v
    return float(mult_w) / sum_w


if __name__ == '__main__':
    weight_average()
