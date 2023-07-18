"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


class Solution:
    """
    >>> Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo")
    True
    >>> Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo")
    False
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counter, length, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    matched += 1
            if i >= length and s2[i - length] in counter:
                if counter[s2[i - length]] == 0:
                    matched -= 1
                counter[s2[i - length]] += 1

            if matched == len(counter):
                return True

        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
