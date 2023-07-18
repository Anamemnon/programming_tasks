"""
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

"""
from typing import List


class Solution:
    """
    >>> Solution().rob([2,3,2])
    3
    >>> Solution().rob([1,2,3,1])
    4
    >>> Solution().rob([1,2,3])
    3
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def rob_(nums: List[int]):
            prev_1, prev_2 = 0, 0

            for money in nums:
                prev_1, prev_2 = max(prev_1, prev_2 + money), prev_1
            return prev_1

        return max(rob_(nums[1:]), rob_(nums[:-1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
