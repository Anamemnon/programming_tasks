"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List


class Solution:
    """
    >>> Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
    [3, 4]
    >>> Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)
    [-1, -1]
    >>> Solution().searchRange(nums = [], target = 0)
    [-1, -1]
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low

        low = search(target)
        high = search(target + 1) - 1

        if low <= high:
            return [low, high]

        return [-1, -1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
