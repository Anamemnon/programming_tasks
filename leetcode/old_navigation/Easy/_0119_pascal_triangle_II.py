"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
"""
from typing import List


class Solution:
    """
    >>> Solution().getRow(3)
    [1, 3, 3, 1]
    """
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1] * i for i in range(1, rowIndex + 2)]

        for i in range(1, rowIndex + 1):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
