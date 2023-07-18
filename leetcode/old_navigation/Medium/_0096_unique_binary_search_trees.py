"""
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.
"""


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]

    # Catalan Number  (2n)!/((n+1)!*n!)
    # https://leetcode.com/problems/unique-binary-search-trees/discuss/703488/Detailed-Explanation-%3A-Mental-Leap-on-Why-the-approach-actually-works
    # def numTrees(self, n):
    #     import math
    #     return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))
