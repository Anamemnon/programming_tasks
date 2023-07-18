"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character



Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def f(i, j):
            if i == 0 and j == 0:
                return 0
            if i == 0 or j == 0:
                return i or j
            if word1[i - 1] == word2[j - 1]:
                return f(i - 1, j - 1)
            return min(1 + f(i, j - 1), 1 + f(i - 1, j), 1 + f(i - 1, j - 1))

        m, n = len(word1), len(word2)
        return f(m, n)
