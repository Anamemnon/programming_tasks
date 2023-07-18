"""
695. Max Area of Island

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return (1 + dfs(grid, row + 1, col) +
                    dfs(grid, row - 1, col) +
                    dfs(grid, row, col + 1) +
                    dfs(grid, row, col - 1))

        n = len(grid)
        m = len(grid[0])

        mn = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mn = max(mn, dfs(grid, i, j))
        return mn

