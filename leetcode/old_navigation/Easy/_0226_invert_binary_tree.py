"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        new_tree = TreeNode(root.val)
        new_tree.left = self.invertTree(root.right)
        new_tree.right = self.invertTree(root.left)
        return new_tree

    """
    def invertTree(self, root):
        if not root or root.left==root.right==None: 
            return root
        
        parent = [root]
        while parent:
            children = []
            for node in parent:
                node.left, node.right = node.right, node.left
                if node.left: 
                    children.append(node.left)
                if node.right: 
                    children.append(node.right)
            parent = children
        return root
    """
