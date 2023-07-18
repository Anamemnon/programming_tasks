"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
"""


class Solution:
    """
    >>> Solution().fib(1)
    1
    >>> Solution().fib(0)
    0
    >>> Solution().fib(2)
    1
    >>> Solution().fib(3)
    2
    >>> Solution().fib(4)
    3
    >>> Solution().fib(6)
    8
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        x1, x2 = 0, 1

        for _ in range(2, n + 1):
            result = x1 + x2
            x1, x2 = x2, result

        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
