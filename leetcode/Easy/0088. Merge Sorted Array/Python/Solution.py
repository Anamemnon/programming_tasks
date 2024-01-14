# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# 88. Merge Sorted Array

from typing import List


class Solution:
    """
    >>> Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    [1, 2, 2, 3, 5, 6]
    >>> Solution().merge([1], 1, [], 0)
    [1]
    >>> Solution().merge([0], 0, [1], 1)
    [1]
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n <= 0:
            return

        p1 = m - 1
        p2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[i], nums1[p1] = nums1[p1], nums1[i]
                p1 -= 1
            elif p2 >= 0:
                nums1[i], nums2[p2] = nums2[p2], nums1[i]
                p2 -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
