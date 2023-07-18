"""
496. Next Greater Element I

The next greater element of some element x in an array is the first greater element
that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""
from typing import List


class Solution:
    """
    >>> Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
    [-1, 3, -1]
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for num1 in nums1:
            index_in_nums2 = nums2.index(num1)
            for num2 in nums2[index_in_nums2 + 1:]:
                if num2 > num1:
                    output.append(num2)
                    break
            else:
                output.append(-1)
        return output


class StackSolution:
    """
    >>> StackSolution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
    [-1, 3, -1]
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}

        for e in nums2:
            while (stack and e > stack[-1]):
                c = stack.pop()
                d[c] = e

            stack.append(e)

        return [d.get(e, -1) for e in nums1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()


