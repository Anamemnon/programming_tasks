"""
1314. Matrix Block Sum

Given a m x n matrix mat and an integer k,
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

    i - k <= r <= i + k,
    j - k <= c <= j + k, and
    (r, c) is a valid position in the matrix.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def solveRow(row, k):
            '''
            O(n)
            Where n is the number of elements in the row
            '''
            n = len(row)
            k = min(k, n)
            newRow = []
            right = k
            left = 0
            total = sum(row[0: right + 1])
            newRow.append(total)

            for index in range(1, n):
                if index > k:
                    total -= row[left]
                    left += 1

                if index < n - k:
                    right += 1
                    total += row[right]
                newRow.append(total)

            return newRow

        ans = [solveRow(row, k) for row in mat]  # O(n*m)
        ans = [solveRow(x, k) for x in zip(*ans)]  # O(n*m)  Transpose
        return [list(x) for x in zip(*ans)]  # Transpose again