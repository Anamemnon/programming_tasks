"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # def postorderTraversal(self, root):
    #     traversal, stack = [], [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             # pre-order, right first
    #             traversal.append(node.val)
    #             stack.append(node.left)
    #             stack.append(node.right)
    #
    #     # reverse result
    #     return traversal[::-1]