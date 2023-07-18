"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
