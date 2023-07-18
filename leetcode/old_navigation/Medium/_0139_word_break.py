"""
139. Word Break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
from typing import List


class Solution:
    """
    >>> Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"])
    True
    >>> Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
    True
    >>> Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
    False
    >>> Solution().wordBreak(s = "bb", wordDict = ["a","b","bbb","bbbb"])
    True
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
