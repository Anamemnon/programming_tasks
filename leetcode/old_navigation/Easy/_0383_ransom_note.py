"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    """
    >>> Solution().canConstruct(ransomNote = "a", magazine = "b")
    False
    >>> Solution().canConstruct(ransomNote = "aa", magazine = "ab")
    False
    >>> Solution().canConstruct(ransomNote = "aa", magazine = "aab")
    True
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
