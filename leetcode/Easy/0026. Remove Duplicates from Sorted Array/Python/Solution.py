from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        >>> Solution().removeDuplicates(nums = [1,1,2])
        [1, 2, 1]
        >>> Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        [0, 1, 2, 3, 4, 0, 1, 1, 2, 3]
        """
        p1 = p2 = 0
        while p1 < len(nums):
            if nums[p1] != nums[p2]:
                p2 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
        return p2 + 1



if __name__ == '__main__':
    import doctest

    doctest.testmod()
