'''
Matrix Multiply (Dot Product)

In mathematics when two matrices are multiplied, the result is a new matrix where each position (i, j) in the output is the sum of the products of the ith _row_ in the first matrix and the jth _column_ in the second.
This is called the [dot product](https://www.mathsisfun.com/algebra/matrix-multiplying.html).
As a follow-up, modify your code to support matrices that are *not* square.
This requires that the number of columns in the first matrix be equal to the number of rows in the second so that the row x column cross products are possible.

EXAMPLE(S)
a = [
  [1, 2],
  [3, 4]
]

b = [
  [5, 6],
  [7, 8]
]

matrixMultiply(a,b) ==
[
  [19,22],
  [43,50]
]

(1 * 1) + (2 * 3) + (3 * 5) =
(1 * 2) + (2 * 4) + (3 * 6) =
(4 * 1) + (5 * 3) + (6 * 5) =
(4 * 2) + (5 * 4) + (6 * 6) =


19 (1,1) = a(1,2) * b(5,7) = 5 + 14 = 19
The (0, 0) position in the result is: 1 * 5 + 2 * 7 = 19
The (0, 1) position in the result is: 1 * 6 + 2 * 8 = 22
The (1, 0) position in the result is: 3 * 5 + 4 * 7 = 43
The (1, 1) position in the result is: 3 * 6 + 4 * 8 = 50
'''

def matrixMultiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    '''
    We assume valid inputs.
    In other words we assume the inputs are of the form
    A (MxN) - M rows by N columns
    B (NxP) - N rows by P columns

    Our output will be of the form
    C (MxP) - M rows by P columns
    '''
    res = []

    # Iterate over each row of a
    for i, row in enumerate(a):
        row_in_product = []

        # Multiply the ith row of a for each column (k) in b
        for k in range(len(a)):
            index_in_product = 0

            # Iterate over each element in the ith row of a
            # Multiplying a[i][j] (the jth element of the ith row)
            # By the kth element in the jth row of matrix b
            for j in range(len(a[0])):
                index_in_product += a[i][j] * b[j][k]

            row_in_product.append(index_in_product)

        res.append(row_in_product)

    return res


assert matrixMultiply([[1, 2],[3, 4]], [[5, 6],[7, 8]]) == [[19,22],[43,50]], "Test one failed."
assert matrixMultiply([[1,2,3],[4,5,6]], [[1,2],[3, 4],[5,6]]) == [[22,28],[49,64]], "Test two failed."
print("All tests passed!")