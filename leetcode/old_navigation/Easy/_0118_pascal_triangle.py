"""
118. Pascal's Triangle


Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
"""
from typing import List


class Solution:
    """
    >>> Solution().generate(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> Solution().generate(1)
    [[1]]
    """

    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * i for i in range(1, numRows + 1)]  # initialize triangle with all 1

        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]  # update each as sum of two elements from above row
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
