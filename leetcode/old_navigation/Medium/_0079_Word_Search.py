"""
79. Word Search
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])

        def backtrack(i, j, idx):
            char = board[i][j]
            if char != word[idx]:
                return False
            elif idx == len(word) - 1:
                return True

            board[i][j] = ''

            if i > 0 and backtrack(i - 1, j, idx + 1):
                return True
            if j > 0 and backtrack(i, j - 1, idx + 1):
                return True
            if i < nrows - 1 and backtrack(i + 1, j, idx + 1):
                return True
            if j < ncols - 1 and backtrack(i, j + 1, idx + 1):
                return True
            board[i][j] = char
            return False

        for i in range(nrows):
            for j in range(ncols):
                if backtrack(i, j, 0):
                    return True

        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        n = len(word)
        visited = set()

        def dfs(r, c, idx):
            if idx > n:
                return False
            visited.add((r, c))
            if idx == n - 1:
                return True
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr, cc = r + dr, c + dc
                if (rr in range(row)
                        and cc in range(col)
                        and (rr, cc) not in visited
                        and board[rr][cc] == word[idx + 1]):
                    if dfs(rr, cc, idx + 1): return True
            visited.remove((r, c))

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
