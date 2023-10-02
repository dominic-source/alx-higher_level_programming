#!/usr/bin/python3

"""This module creates a function to find a peak in a list of unsorted array"""


def find_peak(list_of_integers):
    """This function will find a peak"""

    mlist = list_of_integers
    if not mlist:
        return None
    elif len(mlist) < 2:
        return mlist[0]
    else:
        left = 0
        right = len(mlist) - 1

        while left < right:
            mid = (left + right) // 2

            if mlist[mid] < mlist[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return mlist[left]


def find_peak22(list_of_integers):
    """This function will find a peak"""

    mlist = list_of_integers
    if not mlist:
        return None
    elif len(mlist) < 2:
        return mlist[0]
    elif len(mlist) == 2:
        if mlist[0] < mlist[1]:
            return mlist[1]
        else:
            return mlist[0]
    else:
        for idx in range(len(mlist)):
            value = mlist[idx]
            # find the left and right value of each item
            if idx == 0:
                left = None
            else:
                left = mlist[idx - 1]
            try:
                right = mlist[idx + 1]
            except IndexError:
                right = None

            # find the peak using the left and right
            if left and right:
                if left <= value and value >= right:
                    return value
            elif not left:
                if value >= right:
                    return value
            elif not right:
                if value >= left:
                    return value
