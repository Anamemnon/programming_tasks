# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        from collections import deque
        sum_of_nodes = 0
        q = deque([root])

        while q:
            node = q.popleft()

            if low <= node.val <= high:
                sum_of_nodes += node.val

            if node.left is not None: q.append(node.left)
            if node.right is not None: q.append(node.right)

        return sum_of_nodes
