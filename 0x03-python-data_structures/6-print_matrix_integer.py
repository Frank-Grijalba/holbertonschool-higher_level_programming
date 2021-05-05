#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for i in range(len(matrix)):
            for j in i:
                if j != len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
