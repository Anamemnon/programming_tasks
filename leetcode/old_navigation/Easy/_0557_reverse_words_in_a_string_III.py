"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""
from typing import List


class Solution:
    """
    >>> Solution().reverseWords("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"
    """
    def reverseWords(self, s: str) -> str:
        arr: List[str] = s.split()

        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return " ".join(arr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
