import unittest
import numpy as np
from MatrixCalculator import MatrixCalculator


class TestMatrixCalculator(unittest.TestCase):

    def setUp(self):
        self.matrixCalculator = MatrixCalculator()

    def test_add_matrices(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        expected_result = np.array([[6, 8], [10, 12]])

        self.assertTrue(np.array_equal(self.matrixCalculator.add_matrices(a, b), expected_result))

    def test_multiply_matrices(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        expected_result = np.array([[19, 22], [43, 50]])
        self.assertTrue(np.array_equal(self.matrixCalculator.multiply_matrices(a, b), expected_result))

    def test_transposition_matrix(self):
        a = np.array([[0, 1, 2],
                      [0, 0, 3],
                      [4, 5, 0]])
        expected_result = np.array([[0, 0, 4],
                                    [1, 0, 5],
                                    [2, 3, 0]])
        self.assertTrue(np.array_equal(self.matrixCalculator.transposition_matrix(a), expected_result))

    def test_transform_to_coo(self):
        a = np.array([[0, 1, 2],
                      [0, 0, 3],
                      [4, 5, 0]])
        self.assertTrue(np.array_equal(self.matrixCalculator.transform_to_coo(a).toarray(), a))


if __name__ == '__main__':
    unittest.main()
