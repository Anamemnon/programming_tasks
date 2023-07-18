"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    """
    >>> Solution().tribonacci(0)
    0
    >>> Solution().tribonacci(1)
    1
    >>> Solution().tribonacci(2)
    1
    >>> Solution().tribonacci(3)
    2
    >>> Solution().tribonacci(4)
    4
    >>> Solution().tribonacci(25)
    1389537
    """
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        x1, x2, x3 = 0, 1, 1

        for _ in range(3, n + 1):
            result = x1 + x2 + x3
            x1, x2, x3 = x2, x3, result

        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
