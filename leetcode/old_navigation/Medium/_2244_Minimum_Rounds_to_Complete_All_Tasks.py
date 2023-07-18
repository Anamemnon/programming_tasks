"""
2244. Minimum Rounds to Complete All Tasks

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. 
In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 
Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

 
Constraints:

    1 <= tasks.length <= 105
    1 <= tasks[i] <= 109

"""


from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Counter to hold frequency of ith task and res stores the result.
        table, res = Counter(tasks), 0

        for count in table.values():
            if count <= 1:
                # If count <= 1 then it cannot follow the condition hence return -1.
                return -1

            # Total number of groups increments after 3 values.
            res += ceil(count / 3)

        return res

"""
Explanation: 
Observation:
The question just boils downs to weather the ith task can be done by grouping it into groups of 2 or 3.
Let number of ith tasks be m, a and b are the number of groups of 2's and 3's where a and b can assume any non negative values here. So, m = 2 * a + 3 * b

We can observe that this equation holds true for all values of m for m > 1.

1 = Exception | 2 = 2 * 1 + 3 * 0 | 3 = 2 * 0 + 3 * 1 | 4 = 2 * 2 + 3 * 0 | 5 = 2 * 1 + 3 * 1 | 6 = 2 * 0 + 3 * 2 | 7 = 2 * 2 + 3 * 1 | 8 = 2 * 1 + 3 * 2 | 9 = 2 * 0 + 3 * 3 | 10 = 2 * 2 + 3 * 2 | 11 = 2 * 1 + 3 * 3 | 12 = 2 * 0 + 3 * 4 | 3 * 3 | 14 = 2 * 2 + 3 * 4 | 15 = 2 * 0 + 3 * 5 | 16 = 2 * 2 + 3 * 4 | 17 = 2 * 1 + 3 * 5 

The repeated pattern for 3 consecutive integers here is: A || B || C = 2 x + 3 y || 2 (x-1) + 3 (y+1) || 2 (x-2) + 3 (y+2) [2 goes from x to x-2 while 3 goes from y to y+2] . Look at 1,2,3 and then 4, 5, 6 then 7, 8, 9. They repeat after every 3 values. Also we can notice why this is so: B = A + 1 = A + (3 - 2) . Similarly C = B + 1 = B (3 - 2), since 3 is +ve and 2 is -ve, we have x-1 or 2 for 2 and y+1 or 2 for 3. Thus, total number of groups (x+y) increments after 3 values.

Reason:
Take the base case of m = 2 and 3. They can be divided into group of one 2's and one 3's respectively. Now ontop of this base case add 2 and 3 to m = 2 and 3, we get 2+2 = 4, 2+3=5, 3+3 = 6, three consecutive numbers. Observe that adding 2 and 3 to previous values of m will give new values that will surely be divisible into groups of 2's and 3's as we just added 2 and 3 to a number which previously did follow this condition.
"""