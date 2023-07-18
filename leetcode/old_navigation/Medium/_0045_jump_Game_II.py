"""
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        def get_max_reach(arr):
            out = 0
            for i, v in enumerate(arr):
                out = max(out, (i + 1 + v) - len(arr))
            return out

        dp = []
        curr = 0
        prev = -1
        while curr < len(nums) - 1:
            max_reach = get_max_reach(nums[prev + 1:curr + 1])
            dp.append(max_reach)
            prev = curr
            curr += dp[-1]
            if curr == prev: return 0
        return len(dp)


