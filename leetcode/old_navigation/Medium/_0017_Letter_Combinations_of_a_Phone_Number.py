"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        chars_for_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def helper(curr_digit, curr_str):
            # curr_digit points to index in digits
            # curr_str is the string formed till now
            if curr_digit == len(digits):
                res.append(
                    curr_str)  # Case that we have added a letter corresponding each digit( for digit in digits)
                return
            for i in chars_for_number[digits[curr_digit]]:
                helper(curr_digit + 1, curr_str + i)  # We go to next index and add corresponding letter to curr_str

        helper(0, "")
        return res if digits else []
