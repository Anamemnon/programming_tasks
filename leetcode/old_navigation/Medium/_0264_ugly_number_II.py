"""
264. Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from collections import deque
        if n == 1:
            return 1
        queue2, queue3, queue5 = deque([2]), deque([3]), deque([5])

        for _ in range(1, n):
            result = min(queue2[0], queue3[0], queue5[0])
            if result == queue2[0]:
                queue2.popleft()
            if result == queue3[0]:
                queue3.popleft()
            if result == queue5[0]:
                queue5.popleft()
            queue2.append(result * 2)
            queue3.append(result * 3)
            queue5.append(result * 5)
        return result
