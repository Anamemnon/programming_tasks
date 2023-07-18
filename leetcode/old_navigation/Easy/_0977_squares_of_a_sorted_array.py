"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List


class Solution:
    """
    >>> Solution().sortedSquares([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)

        left, right = 0, len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
