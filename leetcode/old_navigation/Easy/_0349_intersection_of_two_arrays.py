"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


class Solution:
    """
    >>> Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])
    [2]
    >>> Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    [9, 4]
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))


# class Solution:
#     """
#     >>> Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])
#     [2]
#     >>> Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
#     [9, 4]
#     """
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for i in nums1:
#             if i not in res and i in nums2:
#                 res.append(i)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
