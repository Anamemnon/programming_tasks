"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
        return len(matrix) and max(map(max, matrix)) ** 2
