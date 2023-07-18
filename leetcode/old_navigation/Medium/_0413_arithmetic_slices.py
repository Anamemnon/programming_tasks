"""
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

    For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        index = 1
        output = 0
        while index < n:
            count = 1
            diff = nums[index] - nums[index - 1]
            while index < n and nums[index] - nums[index - 1] == diff:
                count += 1
                index += 1
            if count >= 3:
                output += (count - 2) * (count - 1) // 2

        return output
