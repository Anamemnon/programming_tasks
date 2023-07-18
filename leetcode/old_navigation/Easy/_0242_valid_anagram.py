"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    """
    >>> Solution().isAnagram(s = "anagram", t = "nagaram")
    True
    >>> Solution().isAnagram(s = "rat", t = "car")
    False
    >>> Solution().isAnagram(s = "a", t = "ab")
    False
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return all(s.count(c) == t.count(c) for c in set(s))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
