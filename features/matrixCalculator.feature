Feature: Matrix Calculator

  Scenario: Transform matrix to CSR format
     Given calculator and normal matrix
     When we transform matrix to CSR format
     Then matrix is transformed

  Scenario: Transform matrix to BSR format
     Given calculator and normal matrix
     When we transform matrix to BSR format
     Then matrix is transformed

  Scenario: Add csr matrices
     Given calculator and two csr matrices
     When we add csr matrices
     Then result is the sum of the matrices

  Scenario: Multiply csr matrices
     Given calculator and two csr matrices
     When we multiply csr matrices
     Then result is the product of the matrices
