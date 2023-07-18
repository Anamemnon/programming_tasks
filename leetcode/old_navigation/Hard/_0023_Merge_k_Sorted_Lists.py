"""
23. Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104
"""


# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next



class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values, head, pointer = [], None, None

        for l in lists:
            while l:
                heapq.heappush(values, l.val)
                l = l.next

        while values:
            if head is None:
                head = ListNode(heapq.heappop(values))
                pointer = head
            else:
                pointer.next = ListNode(heapq.heappop(values))
                pointer = pointer.next

        return head


class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values, head, pointer = [], None, None

        for l in lists:
            while l:
                values.append(l.val)
                l = l.next

        values.sort()

        while values:
            if head is None:
                head = ListNode(values.pop(0))
                pointer = head
            else:
                pointer.next = ListNode(values.pop(0))
                pointer = pointer.next

        return head