"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    * Starting with any positive integer, replace the number by the sum of the squares of its digits.
    * Repeat the process until the number equals 1 (where it will stay),
        or it loops endlessly in a cycle which does not include 1.
    * Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


class Solution:
    """
    >>> Solution().isHappy(19)
    True
    >>> Solution().isHappy(2)
    False
    """
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
