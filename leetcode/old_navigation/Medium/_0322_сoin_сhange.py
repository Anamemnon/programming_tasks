"""
322. Coin Change

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        queue = deque([(amount, 0)])
        lookup = set([amount])
        while queue:
            remainingAmount, coinsUsed = queue.popleft()
            if remainingAmount == 0:
                return coinsUsed
            for coin in coins:
                if remainingAmount - coin >= 0 and remainingAmount - coin not in lookup:
                    queue.append((remainingAmount - coin, coinsUsed + 1))
                    lookup.add(remainingAmount - coin)

        return -1
