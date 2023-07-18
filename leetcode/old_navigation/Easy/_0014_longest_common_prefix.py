"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    """
    >>> Solution().longestCommonPrefix(strs = ["flower","flow","flight"])
    'fl'
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for tuple_of_chars in list(zip(*strs)):
            if len(set(tuple_of_chars)) == 1:
                prefix += tuple_of_chars[0]
            else:
                return prefix

        return prefix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
