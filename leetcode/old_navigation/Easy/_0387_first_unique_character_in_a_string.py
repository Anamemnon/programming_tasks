"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


class Solution:
    """
    >>> Solution().firstUniqChar("leetcode")
    0
    >>> Solution().firstUniqChar("loveleetcode")
    2
    >>> Solution().firstUniqChar("aabb")
    -1
    """
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        c = {key for key, value in c.items() if value == 1}

        if not c:
            return -1

        for i, v in enumerate(s):
            if v in c:
                return i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
