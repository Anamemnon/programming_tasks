"""
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


class Solution:
    """
    >>> Solution().rotate([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> Solution().rotate([-1,-100,3,99], 2)
    [3, 99, -1, -100]
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Original List                   : 1 2 3 4 5 6 7
        After reversing all numbers     : 7 6 5 4 3 2 1
        After reversing first k numbers : 5 6 7 4 3 2 1
        After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        # for doctests
        # print(nums)

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
