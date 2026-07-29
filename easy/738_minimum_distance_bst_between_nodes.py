"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
Input: root = [4,2,6,1,3]
Output: 1


Strategy: Inorder traversal, and compare each successives pairs.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = list()

        def _inorder(node: Optional[TreeNode]):
            if node is None:
                return None

            _inorder(node.left)
            values.append(node.val)
            _inorder(node.right)

        _inorder(root)

        min_diff = float("inf")

        for i in range(len(values) - 1):
            diff = values[i + 1] - values[i]
            if diff < min_diff:
                min_diff = diff

        return int(min_diff)
