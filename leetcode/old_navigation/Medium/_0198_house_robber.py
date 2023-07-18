"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    """
    >>> Solution().rob([1,2,3,1])
    4
    >>> Solution().rob([2,7,9,3,1])
    12
    """
    def rob(self, nums: List[int]) -> int:
        prev_1, prev_2 = 0, 0

        for money in nums:
            prev_1, prev_2 = max(prev_1, prev_2 + money), prev_1
        return prev_1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
