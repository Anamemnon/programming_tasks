"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character
which is less than any other character (More info).
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_list = {c: i for i, c in enumerate(order)}

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            min_length = min(len(word1), len(word2))

            if (word1[:min_length] == word2[:min_length]) and (len(word1) > len(word2)):
                return False

            for i in range(min_length):
                if word1[i] != word2[i]:
                    if order_list[word1[i]] > order_list[word2[i]]:
                        return False
                    break
        return True
