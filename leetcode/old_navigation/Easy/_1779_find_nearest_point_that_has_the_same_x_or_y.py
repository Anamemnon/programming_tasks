"""
1779. Find Nearest Point That Has the Same X or Y Coordinate

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
"""
from typing import List


class Solution:
    """
    >>> Solution().nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])
    2
    >>> Solution().nearestValidPoint(3, 4, [[3,4]])
    0
    >>> Solution().nearestValidPoint(3, 4, [[2,3]])
    -1
    """
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        def is_valid_point(x1, y1, x2, y2):
            return x1 == x2 or y1 == y2

        smallest_index = -1
        smallest_distance = float('inf')

        for i, (x2, y2) in enumerate(points):
            if not is_valid_point(x, y, x2, y2):
                continue

            distance = manhattan_distance(x, y, x2, y2)
            if distance < smallest_distance:
                smallest_distance = distance
                smallest_index = i

        return smallest_index


if __name__ == '__main__':
    import doctest
    doctest.testmod()
