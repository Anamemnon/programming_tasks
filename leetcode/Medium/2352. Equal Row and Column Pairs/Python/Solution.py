from typing import Counter, List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tpse = Counter(zip(*grid))
        return sum(tpse[row] for row in map(tuple, grid))