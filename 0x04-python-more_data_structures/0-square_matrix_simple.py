#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda x: x ** 2, [m for m in i])) for i in matrix]
    return new_matrix


if __name__ == '__main__':
    square_matrix_simple()
