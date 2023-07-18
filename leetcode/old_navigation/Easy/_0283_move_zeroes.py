"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        >>> Solution().moveZeroes([0,1,0,3,12])
        [1, 3, 12, 0, 0]
        >>> Solution().moveZeroes([0])
        [0]
        """
        last_non_zero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
        # for doctest
        # print(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
