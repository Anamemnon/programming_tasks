"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    """
    >>> Solution().climbStairs(2)
    2
    >>> Solution().climbStairs(3)
    3
    >>> Solution().climbStairs(4)
    5
    """
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1
        if n == 2:
            return 2

        x1 = 1
        x2 = 2
        ways = 0

        for i in range(2, n):
            ways = x1 + x2
            x1, x2 = x2, ways
        return ways


if __name__ == '__main__':
    import doctest
    doctest.testmod()
