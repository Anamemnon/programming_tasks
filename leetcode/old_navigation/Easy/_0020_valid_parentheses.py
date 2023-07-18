"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution:
    """
    >>> Solution().isValid("()")
    True
    >>> Solution().isValid("()[]{}")
    True
    >>> Solution().isValid("(]")
    False
    """

    def isValid(self, s: str) -> bool:
        hash_ = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for v in s:
            if v in hash_:
                stack.append(v)
            elif len(stack) == 0 or hash_[stack.pop()] != v:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    import doctest

    doctest.testmod()
