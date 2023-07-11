from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        >>> Solution().getConcatenation([1,2,1])
        [1, 2, 1, 1, 2, 1]
        """
        return 2 * nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
