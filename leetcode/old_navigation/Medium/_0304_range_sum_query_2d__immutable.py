"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle
    defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2)
    Returns the sum of the elements of matrix inside the rectangle
    defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        row = len(matrix)
        col = len(matrix[0])
        self.dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)