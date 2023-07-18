"""
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""
from typing import List


class Solution:
    """
    >>> Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    11
    >>> Solution().minimumTotal([[-10]])
    -10
    >>> Solution().minimumTotal([[-1],[2,3],[1,-1,-3]])
    -1
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1 <= triangle.length <= 200
        n = len(triangle)
        cur_row, next_row = [0] * n, triangle[n - 1]
        for level in range(n - 2, -1, -1):
            for i in range(level + 1):
                cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i + 1])
            cur_row, next_row = next_row, cur_row
        return next_row[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
