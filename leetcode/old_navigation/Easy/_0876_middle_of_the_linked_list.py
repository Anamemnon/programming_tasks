"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    >>> Solution().middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
    [3,4,5]
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while True:
            arr.append(head)
            if head.next is None:
                break
            head = head.next

        return arr[len(arr) // 2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
