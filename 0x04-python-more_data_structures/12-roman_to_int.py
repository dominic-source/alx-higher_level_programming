#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    i, msum, msr, t = 0, 0, roman_string, len(roman_string)
    while i < t:
        if (t != i + 1) and msr[i] == 'C' and msr[i + 1] == 'M':
            msum += 900
            i += 1
        elif msr[i] == 'M':
            msum += 1000
        elif (t != i + 1) and msr[i] == 'C' and msr[i + 1] == 'D':
            msum += 400
            i += 1
        elif msr[i] == 'D':
            msum += 500
        elif (t != i + 1) and msr[i] == 'X' and msr[i + 1] == 'C':
            msum += 90
            i += 1
        elif msr[i] == 'C':
            msum += 100
        elif (t != i + 1) and msr[i] == 'X' and msr[i + 1] == 'L':
            msum += 40
            i += 1
        elif msr[i] == 'L':
            msum += 50
        elif (t != i + 1) and msr[i] == 'I' and msr[i + 1] == 'X':
            msum += 9
            i += 1
        elif msr[i] == 'X':
            msum += 10
        elif (t != i + 1) and msr[i] == 'I' and msr[i + 1] == 'V':
            msum += 4
            i += 1
        elif msr[i] == 'V':
            msum += 5
        elif msr[i] == 'I':
            msum += 1
        i += 1
    return msum


if __name__ == '__main__':
    roman_to_int('LXXXVII')
