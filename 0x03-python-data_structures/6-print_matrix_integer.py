#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for d, n in enumerate(i):
            if d != 0:
                print(' ', end='')
            print('{:d}'.format(n), end='')
        print('')


if __name__ == '__main__':
    print_matrix_integer()
