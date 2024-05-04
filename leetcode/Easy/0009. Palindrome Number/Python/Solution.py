class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)

        for v1, v2 in zip(s, reversed(s)):
            if v1 != v2:
                return False

        return True
