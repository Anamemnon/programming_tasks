"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""


class Solution:
    """
    >>> Solution().countOdds(3, 7)
    3
    >>> Solution().countOdds(8, 10)
    1
    """
    def countOdds(self, low: int, high: int) -> int:
        count = 0

        if low % 2 != 0:
            count += 1
            low += 1

        if high % 2 != 0:
            count += 1
            high -= 1

        count += int((high - low) / 2)
        return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
