"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List


class Solution:
    """
    >>> Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
    6
    >>> Solution().trap(height = [4,2,0,3,2,5])
    9
    """
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i, v in enumerate(height):
            # we need to see if we can form a container
            while stack and v >= stack[-1][0]:
                popped, _ = stack.pop()
                # is it a container though? we have a left border?
                if stack:
                    left_border, j = stack[-1]
                    # we compute the water
                    water += min(left_border - popped, v - popped) * (i - j - 1)
            stack.append((v, i))
        return water


if __name__ == '__main__':
    import doctest
    doctest.testmod()
