"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    """
    >>> Solution().twoSum([2,7,11,15], 9)
    [0, 1]
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, v in enumerate(nums):
            y = target - v
            if y in hash_table:
                return [hash_table[y], i]
            else:
                hash_table[v] = i

        return []

if __name__ == '__main__':
    import doctest
    doctest.testmod()
