"""
566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one
with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows
and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List


class Solution:
    """
    >>> Solution().matrixReshape([[1,2],[3,4]], 1, 4)
    [[1, 2, 3, 4]]
    >>> Solution().matrixReshape([[1, 2, 3, 4]], 2, 4)
    [[1, 2, 3, 4]]
    """

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def yielder(m: List[List[int]]):
            for row in m:
                for value in row:
                    yield value

        if not mat:
            return []

        if len(mat) * len((mat[0])) != r * c:
            return mat

        gen = yielder(mat)
        return [[next(gen) for _ in range(c)] for _ in range(r)]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
