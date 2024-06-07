from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        prev = chars[-1]
        n = 1
        p1 = len(chars) - 1
        i = p1 - 1
        while i >= 0:
            if chars[i] != prev:
                if n > 1:
                    chars[i + 1:p1 + 1] = [prev] + [ch for ch in str(n)]

                n = 0
                prev = chars[i]
                p1 = i
            n += 1
            i -= 1

        if n > 1:
            chars[0:p1 + 1] = [prev] + [ch for ch in str(n)]

        return len(chars)
