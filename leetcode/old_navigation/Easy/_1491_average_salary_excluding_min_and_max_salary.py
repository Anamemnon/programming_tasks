"""1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10^-5 of the actual answer will be accepted.
"""
from typing import List


class Solution:
    """
    >>> Solution().average([4000,3000,1000,2000])
    2500.0
    >>> Solution().average([1000,2000,3000])
    2000.0
    """
    def average(self, salary: List[int]) -> float:
        min_ = max_ = salary[0]

        for v in salary[1:]:
            if v < min_:
                min_ = v
            if v > max_:
                max_ = v

        return (sum(salary) - (min_ + max_)) / (len(salary) - 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
