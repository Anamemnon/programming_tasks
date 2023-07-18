"""
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
import queue
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        queue = deque([root])
        res = []

        while queue:
            node = queue.pop()
            if node is not None:
                res.append(node.val)
                queue.append(node.right)
                queue.append(node.left)

        return res

    # recursive solution
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #
    #     def dfs(root: Optional[TreeNode]):
    #         if not root:
    #             return
    #
    #         res.append(root.val)
    #
    #         dfs(root.left)
    #         dfs(root.right)
    #
    #     dfs(root)
    #     return res
