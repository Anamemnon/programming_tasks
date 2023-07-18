"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == '__main__':
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9)
