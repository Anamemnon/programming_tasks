"""
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        if x == 0: return 0
        val = x
        while True:
            last = val
            val = (val + x / val) * 0.5
            if abs(val - last) < 1e-2:
                return int(val)
        """
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                high = mid - 1
            else:
                low = mid + 1

        return mid
