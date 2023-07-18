"""
1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
from typing import List


class Solution:
    """
    >>> Solution().arraySign([-1,-2,-3,-4,3,2,1])
    1
    >>> Solution().arraySign([1,5,0,2,-3])
    0
    >>> Solution().arraySign([-1,1,-1,1,-1])
    -1
    """
    def arraySign(self, nums: List[int]) -> int:
        neg = 0

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                neg += 1

        if neg % 2 == 0:
            return 1
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
