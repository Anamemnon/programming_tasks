"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary diagonal.
"""
from typing import List


class Solution:
    """
    >>> Solution().diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
    25
    >>> Solution().diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
    8
    """
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0

        for i in range(len(mat)):
            s += mat[i][i]

        for i in range(len(mat)):
            s += mat[len(mat) - i - 1][i]

        if len(mat) % 2 == 1:
            s -= mat[len(mat) // 2][len(mat) // 2]

        return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
