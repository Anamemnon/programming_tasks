"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = ListNode()
        runner = head

        while list1 and list2:
            if list1.val < list2.val:
                runner.next = ListNode(list1.val)
                list1 = list1.next
            else:
                runner.next = ListNode(list2.val)
                list2 = list2.next

            runner = runner.next

        runner.next = list1 or list2
        return head.next



