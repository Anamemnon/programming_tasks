"""
2. Add Two Numbers
 https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    >>> Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
    ListNode(7, ListNode(0, ListNode(8)))
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_val = 0
        root = curr = ListNode(0)

        while l1 or l2 or sum_val:
            if l1:
                sum_val += l1.val
                l1 = l1.next

            if l2:
                sum_val += l2.val
                l2 = l2.next

            curr.next = curr = ListNode(sum_val % 10)
            sum_val //= 10
        return root.next


if __name__ == '__main__':
    import doctest
    doctest.testmod()
