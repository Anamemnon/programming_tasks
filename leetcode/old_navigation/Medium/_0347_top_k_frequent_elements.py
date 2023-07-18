"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]



Constraints:

    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

"""
from typing import List


class Solution:
    """
    >>> Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
    [1, 2]
    >>> Solution().topKFrequent(nums = [1], k = 1)
    [1]
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        return [key for (key, _) in Counter(nums).most_common(k)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
