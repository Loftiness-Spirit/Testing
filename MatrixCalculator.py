import numpy as np
import scipy as sc
# Матричный калькулятор (операции с матрицами, в том числе с разреженными).


class MatrixCalculator:
    def __init__(self):
        pass

    def add_matrices(self, matrix1, matrix2):
        return matrix1 + matrix2

    def multiply_matrices(self, matrix1, matrix2):
        return np.dot(matrix1, matrix2)

    def transposition_matrix(self, matrix):
        return matrix.transpose()

    def transform_to_coo(self, matrix):
        return sc.sparse.coo_matrix(matrix)

    def transform_to_csr(self, matrix):
        return sc.sparse.csr_matrix(matrix)

    def transform_to_bsr(self, matrix):
        return sc.sparse.bsr_matrix(matrix)

    def add_csr_matrices(self, matrix1, matrix2):
        return matrix1 + matrix2

    def multiply_csr_matrices(self, matrix1, matrix2):
        return sc.sparse.csr_matrix.dot(matrix1, matrix2)


if __name__ == '__main__':
    pass
