from behave import *
import numpy as np
import scipy as sc
from MatrixCalculator import MatrixCalculator


@given('Calculator and normal matrix')
def step_given_matrix(context):
    context.matrixCalculator = MatrixCalculator()
    context.A = [[0, 1, 2],
                 [0, 0, 3],
                 [4, 5, 0]]


@when('we transform matrix to CSR format')
def step_when_transform_to_csr(context):
    context.result = context.matrixCalculator.transform_to_csr(context.A)


@when('we transform matrix to BSR format')
def step_when_transform_to_csr(context):
    context.result = context.matrixCalculator.transform_to_bsr(context.A)


@then('matrix is transformed')
def step_then_check_transform_result(context):
    assert (np.array_equal(context.result.toarray(), context.A))


@given('calculator and two csr matrices')
def step_given_matrices(context):
    context.matrixCalculator = MatrixCalculator()
    context.A = sc.sparse.csr_matrix([[0, 1, 2],
                                      [0, 0, 3],
                                      [4, 5, 0]])
    context.B = sc.sparse.csr_matrix([[6, 0, 0],
                                      [0, 7, 0],
                                      [9, 0, 8]])


@when('we add csr matrices')
def step_when_csr_add(context):
    context.result = context.matrixCalculator.add_csr_matrices(context.A, context.B)


@then('result is the sum of the matrices')
def step_then_check_sum_result(context):
    assert (np.array_equal(context.result.toarray(), [[6, 1, 2],
                                                      [0, 7, 3],
                                                      [13, 5, 8]]))


@when('we multiply csr matrices')
def step_when_csr_multiply(context):
    context.result = context.matrixCalculator.multiply_csr_matrices(context.A, context.B)


@then('result is the product of the matrices')
def step_then_check_product_result(context):
    assert (np.array_equal(context.result.toarray(), [[18, 7, 16],
                                                      [27, 0, 24],
                                                      [24, 35, 0]]))
