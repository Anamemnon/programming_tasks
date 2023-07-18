"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            if root.val == val:
                return root

            return dfs(root.right) or dfs(root.left)
        return dfs(root)

    """
    def iterative(self, root, val):
        temp = root
        while temp:
            if temp.val == val: 
                return temp
            elif temp.val < val: 
                temp = temp.right
            else: 
                temp = temp.left
        return None
    """