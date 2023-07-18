"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from typing import List


class Solution:
    """
    >>> Solution().twoSum([2,7,11,15], 9)
    [1, 2]
    >>> Solution().twoSum([2,3,4], 6)
    [1, 3]
    >>> Solution().twoSum([-1,0], -1)
    [1, 2]
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        for _ in range(len(numbers)):
            sum_ = numbers[p1] + numbers[p2]
            if sum_ > target:
                p2 -= 1
            elif sum_ < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]

        return [-1, -1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
