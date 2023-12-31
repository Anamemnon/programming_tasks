"""
852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain,
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].


Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
"""
from typing import List


class Solution:
    """
    >>> Solution().peakIndexInMountainArray(arr = [0,1,0])
    1
    >>> Solution().peakIndexInMountainArray(arr = [0,2,1,0])
    1
    >>> Solution().peakIndexInMountainArray(arr = [0,10,5,2])
    1
    >>> Solution().peakIndexInMountainArray(arr = [3,9,8,6,4])
    1
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    import doctest
    doctest.testmod()
