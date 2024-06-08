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
        p1 = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
        # for doctest
        # print(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
