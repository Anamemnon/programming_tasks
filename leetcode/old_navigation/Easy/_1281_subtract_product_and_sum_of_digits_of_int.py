"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


class Solution:
    """
    >>> Solution().subtractProductAndSum(234)
    15
    >>> Solution().subtractProductAndSum(4421)
    21
    """
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)

        product = 1
        sum_ = 0

        for digit in s:
            sum_ += int(digit)
            product *= int(digit)

        return product - sum_


if __name__ == '__main__':
    import doctest
    doctest.testmod()
