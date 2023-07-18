"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            r = r[::-1] if len(res) % 2 else r
            if r:
                res.append(r)
        return res
