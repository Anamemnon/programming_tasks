"""
Given a non-empty 2D array grid of 0’s and 1’s, an island is a group of 1’s (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island
can be translated (and not rotated or reflected) to equal the other.

Sample I/O
Example 1

11000
11000
00011
00011

Given the above grid map, return 1.

Example 2

11011
10000
00001
11011

Given the above grid map, return 3.

The length of each dimension in the given grid does not exceed 50.
"""
from typing import List


def numDistinctIslands(self, grid: List[List[int]]) -> int:
    row = len(grid)
    col = len(grid[0])
    shapes = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    def dfs(x, y, pos, island_direction):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] and (nx, ny) not in visited:
                temp_direction = (pos[0] + dx, pos[1] + dy)
                visited.add((nx, ny))
                island_direction.append(temp_direction)
                dfs(nx, ny, temp_direction, island_direction)
        return tuple(island_direction)

    for x in range(row):
        for y in range(col):
            if grid[x][y] and (x, y) not in visited:
                visited.add((x, y))
                shapes.add(dfs(x, y, (0, 0), [(0, 0)]))
    return len(shapes)
