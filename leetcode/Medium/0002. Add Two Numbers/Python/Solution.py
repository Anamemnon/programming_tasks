# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_n = 0
        l2_n = 0

        i = 0
        while l1:
            l1_n += l1.val * 10 ** i
            i += 1
            l1 = l1.next

        i = 0
        while l2:
            l2_n += l2.val * 10 ** i
            i += 1
            l2 = l2.next

        res_n = l1_n + l2_n

        root =  ListNode(val=res_n % 10)
        res = root
        res_n //= 10

        while res_n:
            res.next = ListNode(val=res_n % 10)
            res = res.next
            res_n //= 10
        return root


if __name__ == '__main__':
    r = Solution().addTwoNumbers(l1 = ListNode(2, ListNode(4, ListNode(3))),
                                 l2 = ListNode(5, ListNode(6, ListNode(4))),)
    print(r)