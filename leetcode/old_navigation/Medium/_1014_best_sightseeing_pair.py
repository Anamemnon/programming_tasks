"""
1014. Best Sightseeing Pair

You are given an integer array values where values[i] represents the value of the ith sightseeing spot.
Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:
Input: values = [1,2]
Output: 2
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        cur_max = values[0] - 1
        for v in values[1:]:
            ans = max(ans, v + cur_max)
            if v >= cur_max:
                cur_max = v - 1
            else:
                cur_max -= 1
        return ans