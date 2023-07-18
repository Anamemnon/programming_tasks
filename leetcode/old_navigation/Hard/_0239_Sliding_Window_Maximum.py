"""
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""

from typing import List


class Solution1:
    """
    Brute Force O(kn)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return nums and [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## RC ##
        ## APPROACH : DEQUE ##
        """
            ## LOGIC ##
            1. For the First k numbers we can directly find maximum and store, but the when the window slides by one position, the first element is removed.
                What if the first number is the maximum of 0 to K ? How do we know the second maximum when first element is removed ? ( consider this example: [5, 2, 3, -1] and k = 3 ans = [5, 3] )
                So, For that we need to maintain some storage, here we use deque.
            2. Our Deque will always have the maximum at the start and we append small elements next to it.
                ( if deque(for now, say we have numbers in it) is [4,1,0] and incoming curr num is 2, pop all nums smaller from backside i.e deque will be [4, 2] )
            3. And when the window slides, we remove all the numbers from front of deque if they donot fall under this window size.

            Example : [1,3,1,2,0,5] 3
            deque([0])              [1]
            deque([1])              [1, 3]
            deque([1, 2])           [1, 3, 3]
            deque([1, 3])           [1, 3, 3, 3]
            deque([3, 4])           [1, 3, 3, 3, 2]
            deque([5])              [1, 3, 3, 3, 2, 5]

            ## TIME COMPLEXITY : O(N) ##
            ## SPACE COMPLEXITY : O(k) ##
        """
        import collections
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:
                deque.pop()     # 2
            if deque and i - deque[0] >= k:
                deque.popleft() # 3

            deque.append(i)
            res.append(nums[deque[0]])
            # print(deque, res)
        return res[k-1:]