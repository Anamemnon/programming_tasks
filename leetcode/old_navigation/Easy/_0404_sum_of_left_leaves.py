"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root or (root.left is None and root.right is None):
            return 0

        res, stack = 0, [root]

        while stack:
            node = stack.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    res += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res
    """

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, flag):
            nonlocal ans
            if not root: return
            if flag and not root.left and not root.right:
                ans += root.val
            dfs(root.left, 1)
            dfs(root.right, 0)

        dfs(root, 0)
        return ans
