"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from typing import List


class Solution:
    """
    >>> Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    >>> Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])
    [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        # Calculate the TOP/LEFT adjacents
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != 0:
                    top = mat[row - 1][col] if row > 0 else float('inf')
                    left = mat[row][col - 1] if col > 0 else float('inf')

                    mat[row][col] = min(top, left) + 1

        # Calcualte the BOTTOM/RIGHT adjacents
        for row in range(rows)[::-1]:
            for col in range(cols)[::-1]:
                if mat[row][col] != 0:
                    bottom = mat[row + 1][col] if row < rows - 1 else float('inf')
                    right = mat[row][col + 1] if col < cols - 1 else float('inf')

                    mat[row][col] = min(mat[row][col], min(bottom, right) + 1)

        return mat


if __name__ == '__main__':
    import doctest
    doctest.testmod()
