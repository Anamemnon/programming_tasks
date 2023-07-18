"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing
at most one string swap on exactly one of the strings. Otherwise, return false.
"""


class Solution:
    """
    >>> Solution().areAlmostEqual("bank", "kanb")
    True
    >>> Solution().areAlmostEqual("attack", "defend")
    False
    >>> Solution().areAlmostEqual("kelb", "kelb")
    True
    """
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        first_index = -1
        second_index = -1

        for i, v in enumerate(s1):
            if first_index >= 0 and second_index >= 0:
                break

            if v != s2[i]:
                if first_index == -1:
                    first_index = i
                else:
                    second_index = i
        s1 = s1[:first_index] + s1[second_index] + s1[first_index + 1:second_index] + s1[first_index] + s1[second_index + 1:]
        return s1 == s2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
