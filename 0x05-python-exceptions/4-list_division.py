#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r = 0
    new_list = []
    while r < list_length:
        try:
            result = my_list_1[r] / my_list_2[r]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            r += 1
    return new_list
