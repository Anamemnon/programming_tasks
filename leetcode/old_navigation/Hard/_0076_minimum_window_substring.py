"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    """
    >>> Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
    'BANC'
    """
    def minWindow(self, s: str, t: str) -> str:
        import collections

        need = collections.Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):  # index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # match all chars
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1  # make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

