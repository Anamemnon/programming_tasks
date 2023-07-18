"""
976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
"""
from typing import List


class Solution:
    """
    >>> Solution().largestPerimeter([2,1,2])
    5
    >>> Solution().largestPerimeter([1,2,1])
    0
    """
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(3, len(nums) + 1):
            if nums[i - 3] < nums[i - 2] + nums[i - 1]:
                return sum(nums[i - 3: i])
        return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

