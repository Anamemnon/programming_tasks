"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        free, last, now = 0, 0, 0  # profit values (before the cooldown, in our last step, and now)
        for x in prices:
            now = max(last, x - buy)
            buy = min(buy, x - free)
            free, last = last, now
        return now