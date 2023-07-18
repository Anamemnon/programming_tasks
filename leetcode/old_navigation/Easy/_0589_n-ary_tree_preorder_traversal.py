"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Recursive Solution
class Solution:
    """
    >>> Solution().preorder(Node(1, [Node(3, [Node(5,[]), Node(6, [])]), Node(2, []), Node(4, [])]))
    [1, 3, 5, 6, 2, 4]
    """
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root: Node, output: List):
            if root is None:
                return

            output.append(root.val)

            for child in root.children:
                dfs(child, output)

        output = []

        dfs(root, output)

        return output


# Recursive Solution
class IterativeSolution:
    """
    >>> IterativeSolution().preorder(Node(1, [Node(3, [Node(5,[]), Node(6, [])]), Node(2, []), Node(4, [])]))
    [1, 3, 5, 6, 2, 4]
    """
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)

            # add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(node.children[::-1])

        return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
