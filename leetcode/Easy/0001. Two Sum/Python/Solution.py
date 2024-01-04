from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, v in enumerate(nums):
            key = target - v
            if key in d:
                return [d[key], i]

            d[v] = i


if __name__ == '__main__':
    print(Solution().twoSum(nums = [2,7,11,15], target = 9))
    print(Solution().twoSum(nums = [3,2,4], target = 6))
    print(Solution().twoSum(nums = [3,3], target = 6))
