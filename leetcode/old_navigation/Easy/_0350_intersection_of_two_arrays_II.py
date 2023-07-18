"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> Solution().intersect([1,2,2,1], [2,2])
        [2, 2]
        >>> Solution().intersect([4,9,5], [9,4,9,8,4])
        [4, 9]
        """
        import collections
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
