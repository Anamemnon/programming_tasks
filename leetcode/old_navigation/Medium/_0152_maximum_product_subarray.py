"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


class Solution:
    """
    >>> Solution().maxProduct([2,3,-2,4])
    6
    >>> Solution().maxProduct([-2,0,-1])
    0
    """
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = prev_min = ans = nums[0]

        for v in nums[1:]:
            curr_max = max(max(prev_max * v, prev_min * v), v)
            curr_min = min(min(prev_max * v, prev_min * v), v)
            prev_max = curr_max
            prev_min = curr_min
            ans = max(ans, curr_max)
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
