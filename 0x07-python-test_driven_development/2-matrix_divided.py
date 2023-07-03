#!/usr/bin/python3

"""The matrix module

The matrix will be divided by div

Args:
    matrix (list): a list of list
    div (int|float): the number to the divide the list by

"""

def matrix_divided(matrix, div):
    """This will divide each element of the matrix"""

    new_matrix = []
    size = None
    if (not isinstance(matrix, list)) or (matrix is None):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        unit_matrix = []
        if size is None:
            size = len(i)
        elif size < len(i) or size > len(i):
            raise TypeError("Each row of the matrix must have the same size")
        if not (isinstance(matrix, list)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for m in i:
            if not ((isinstance(m, int)) or (isinstance(m, float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            unit_matrix.append(round(m / div, 2))
        new_matrix.append(unit_matrix)
    return new_matrix
