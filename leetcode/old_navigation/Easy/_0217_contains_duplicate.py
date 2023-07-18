"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List


class Solution:
    """
    >>> Solution().containsDuplicate([1,2,3,1])
    True
    >>> Solution().containsDuplicate([1,2,3,4])
    False
    >>> Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()

        for i in nums:
            if i in distinct:
                return True
            distinct.add(i)

        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()