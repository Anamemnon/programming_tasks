import heapq
import statistics
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = heapq.merge(nums1, nums2)
        return statistics.median(merged)
