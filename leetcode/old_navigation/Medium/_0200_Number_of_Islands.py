"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    self.dfs(grid, row, col, visited)
        return islands

    def dfs(self, grid, row, col, visited):
        if (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
                and (row, col) not in visited and grid[row][col] == '1'):
            visited.add((row, col))
            self.dfs(grid, row + 1, col, visited)
            self.dfs(grid, row - 1, col, visited)
            self.dfs(grid, row, col + 1, visited)
            self.dfs(grid, row, col - 1, visited)

"""
Many of the solutions from other users (and the official solution) involve updating elements in the grid to '0' to mark them as "visited".

In practice, this is a poor choice, as it modifies the input data as a side-effect of the solution.

Unless you have been explicitly told to modify some input "in-place", you should avoid this.

In my solution I chose to use a Set of tuples of (row, col) to keep track of each element I've already visited.

You might be asking: "Doesn't this add to the overall memory usage of the solution?"

And the answer would be "yes", however it does not increase the space complexity of the solution.

Since we're doing a DFS to mark each "island", we already have a space complexity of O(M x N); 
in the worst-case our DFS will visit every element in the grid and thus make M x N recursive calls.

Adding on an additional M x N space by tracking the "visited" elements in a Set (you could also use an additional 2D list/array), 
does not increase the space complexity. This is because when we assess the "Big O" space of a solution, we drop constant terms.

A solution that is O(2 x M x N) is still considered O(M x N).
"""


# one more solution
class Solution:
    # one more solution
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
