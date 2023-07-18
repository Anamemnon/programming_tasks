"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import bisect
        import collections
        dp = []
        d = collections.defaultdict(list)
        for i, c in enumerate(text2):
            d[c].append(i)
        for c in text1:
            if c in d:
                for i in reversed(d[c]):
                    ins = bisect.bisect_left(dp, i)
                    if ins == len(dp):
                        dp.append(i)
                    else:
                        dp[ins] = i
        return len(dp)
