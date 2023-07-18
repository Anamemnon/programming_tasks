"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
"""
from typing import List


class Solution:
    """
    >>> Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> Solution().countNegatives([[3,2],[1,0]])
    0
    >>> Solution().countNegatives([[4,3,2,1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    7
    >>> Solution().countNegatives([[4,3,2,1],[3,2,1,-1],[1,-1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> Solution().countNegatives([[3,-1,-3,-3,-3],[2,-2,-3,-3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]])
    16
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            if row[-1] >= 0:
                continue
            low, high = 0, len(row) - 1

            while low < high:
                mid = low + (high - low) // 2
                if row[mid] < 0:
                    high = mid
                else:
                    low = mid + 1
            count += len(row) - low

        return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
