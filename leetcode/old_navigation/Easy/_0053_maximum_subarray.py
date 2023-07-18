"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
 which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List


class Solution:
    """
    >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> Solution().maxSubArray([1])
    1
    >>> Solution().maxSubArray([5,4,-1,7,8])
    6
    """
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum


if __name__ == '__main__':
    import doctest
    doctest.testmod()
