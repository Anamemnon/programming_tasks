"""
1309. Decrypt String from Alphabet to Integer Mapping

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"
"""


class Solution:
    """
    >>> Solution().freqAlphabets(s = "10#11#12")
    'jkab'
    >>> Solution().freqAlphabets(s = "1326#")
    'acz'
    """
    def freqAlphabets(self, s: str) -> str:
        ind_a = 97 - 1
        res = []

        i = 0
        while i < len(s):
            if '#' in s[i:i+3]:
                res.append(chr(ind_a + int(s[i] + s[i + 1])))
                i += 3
            else:
                res.append(chr(ind_a + int(s[i])))
                i += 1

        return "".join(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
