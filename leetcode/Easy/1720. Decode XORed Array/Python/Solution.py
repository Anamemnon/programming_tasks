from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        >>> Solution().decode(encoded = [1,2,3], first = 1)
        [1, 0, 2, 1]
        >>> Solution().decode(encoded = [6,2,7,3], first = 4)
        [4, 2, 0, 7, 4]
        """
        arr = [0] * (len(encoded) + 1)

        arr[0] = first

        for i, v in enumerate(encoded, start=1):
            arr[i] = arr[i - 1] ^ v

        return arr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
