"""
63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]  # DP Matrix of size m*n intialized to 0
        dp[0][0] = 1

        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] += dp[r - 1][c] if r - 1 >= 0 else 0
                    dp[r][c] += dp[r][c - 1] if c - 1 >= 0 else 0

        return dp[-1][-1]