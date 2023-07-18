"""
1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression
if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false.
"""
from typing import List


class Solution:
    """
    >>> Solution().canMakeArithmeticProgression([3,5,1])
    True
    >>> Solution().canMakeArithmeticProgression([1,2,4])
    False
    """
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = abs(arr[0] - arr[1])

        for i in range(1, len(arr)):
            if abs(arr[i - 1] - arr[i]) != diff:
                return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
