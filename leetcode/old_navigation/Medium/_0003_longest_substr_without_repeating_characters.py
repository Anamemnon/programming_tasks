"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    """
    >>> Solution().lengthOfLongestSubstring("abcabcbb")
    3
    >>> Solution().lengthOfLongestSubstring("bbbbb")
    1
    >>> Solution().lengthOfLongestSubstring("pwwkew")
    3
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = -1

        max_len = 0
        used = {}

        for p2, v in enumerate(s):
            old_index = used.get(v, p2)
            used[v] = p2

            if old_index != p2:
                p1 = max(p1, old_index)

            max_len = max(max_len, p2 - p1)

        return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()
