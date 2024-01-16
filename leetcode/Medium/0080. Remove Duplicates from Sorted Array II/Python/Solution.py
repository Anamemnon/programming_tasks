from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = p2 = 0

        while p1 < len(nums):
            if p2 < 2 or nums[p2 - 2] != nums[p1]:
                nums[p2] = nums[p1]
                p2 += 1
            p1 += 1

        return p2