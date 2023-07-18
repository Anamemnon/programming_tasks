"""
784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
"""
from typing import List


class Solution:
    """
    >>> Solution().letterCasePermutation(s = "a1b2")
    ['A1B2', 'a1B2', 'A1b2', 'a1b2']
    >>> Solution().letterCasePermutation(s = "3z4")
    ['3Z4', '3z4']
    """
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        for ch in s:
            for i in range(len(output)):
                if ch.isalpha():
                    output.append(output[i] + ch.lower())
                    output[i] = output[i] + ch.upper()
                else:
                    output[i] = output[i] + ch
        return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
