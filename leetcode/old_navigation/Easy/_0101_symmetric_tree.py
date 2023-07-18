"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left and right:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            return left == right

        if not root:
            return True
        return dfs(root.left, root.right)


    """
    def isSymmetric(self, root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.val != r.val):
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True
    """