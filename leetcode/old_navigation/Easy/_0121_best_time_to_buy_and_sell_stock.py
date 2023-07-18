"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


class Solution:
    """
    >>> Solution().maxProfit([7,1,5,3,6,4])
    5
    >>> Solution().maxProfit([7,6,4,3,1])
    0
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    import doctest
    doctest.testmod()

