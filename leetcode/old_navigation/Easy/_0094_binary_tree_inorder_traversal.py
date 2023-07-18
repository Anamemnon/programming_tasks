"""
94. Binary Tree Inorder Traversal

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        node = root

        while node or stack:
            while node:  # put all left nodes in the stack
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res