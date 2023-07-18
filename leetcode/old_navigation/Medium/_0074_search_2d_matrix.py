"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""
from typing import List


class Solution:
    """
    >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    True
    >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    False
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, low, high = -1, 0, m - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        if row == -1:
            return False

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
