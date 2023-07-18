"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Loop through every cost after the first two steps
        for i in range(2, len(cost)):
            # Update the cheapest cost to step here
            cost[i] += min(cost[i - 2], cost[i - 1])

        # Cheapest cost of the last two steps is the answer
        return min(cost[len(cost) - 2], cost[len(cost) - 1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
