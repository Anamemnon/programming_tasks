"""
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Note:

    Note that in some languages, such as Java, there is no unsigned integer type.
    In this case, the input will be given as a signed integer type.
    It should not affect your implementation, as the integer's internal binary representation is the same,
    whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation.
    Therefore, in Example 3, the input represents the signed integer. -3.
"""


class Solution:
    """
    >>> Solution().hammingWeight(11)
    3
    """
    def hammingWeight(self, n: int) -> int:
        """
        answer = 0
        while n != 0:
            answer += n % 2
            n >>= 1
        return answer
        """
        return n.bit_count()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

