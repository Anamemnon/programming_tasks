"""
112. Path Sum

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    """
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [[root, targetSum - root.val]]
        while stack:
            cur, curr_sum = stack.pop()
            if not cur.left and not cur.right and curr_sum == 0:
                return True
            if cur.right:
                stack.append((cur.right, curr_sum - cur.right.val))
            if cur.left:
                stack.append((cur.left, curr_sum - cur.left.val))
        return False
    """