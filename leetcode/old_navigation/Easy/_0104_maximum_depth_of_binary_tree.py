"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    # iterative solution
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        worklist = deque([root])
        num_node_level = 1
        levels = 0
        while worklist:
            node = worklist.popleft()
            if node.left:
                worklist.append(node.left)
            if node.right:
                worklist.append(node.right)
            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)

        return levels
    """

    """
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            return max(left, right)

        return dfs(root)
