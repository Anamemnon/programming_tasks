"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
"""
from typing import List


class Solution:
    """
    >>> Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
    True
    >>> Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
    False
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        """
        if it's a line, then
        (y - y0)   (y1 - y0)
        -------- = --------
        (x - x0)   (x1 - x0)
        """
        for x, y in coordinates[2:]:
            if (y1 - y0) * (x - x0) != (x1 - x0) * (y - y0):
                return False

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
