"""
343. Integer Break

Given an integer n, break it into the sum of k positive integers,
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1  # must break into 1 & (n-1)

        num_3 = n // 3  # break the number into (3+3+3+...) + remainder

        if n % 3 == 0:
            return 3 ** num_3  # (3+3+3+...)
        if n % 3 == 2:
            return (3 ** num_3) * 2  # (3+3+3+...) + 2
        if n % 3 == 1:
            return 3 ** (num_3 - 1) * 4  # (3+3+3+...) + 1 --> (3+3+...) + 3 + 1 -- > (3+3+...) + 4