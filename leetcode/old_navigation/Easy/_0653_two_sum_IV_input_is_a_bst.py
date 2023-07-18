"""
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        from collections import deque

        if root is None:
            return False

        q = deque()
        q.append(root)
        q_set = set()

        # BFS Traversal
        while q:
            temp: TreeNode = q.popleft()

            if k - temp.val in q_set:
                return True
            else:
                q_set.add(temp.val)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        return False
