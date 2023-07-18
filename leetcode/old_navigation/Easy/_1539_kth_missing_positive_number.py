"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
from typing import List


class Solution:
    """
    >>> Solution().findKthPositive(arr = [2,3,4,7,11], k = 5)
    9
    >>> Solution().findKthPositive(arr = [1,2,3,4], k = 2)
    6
    """
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k


if __name__ == '__main__':
    import doctest
    doctest.testmod()
