"""Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

from typing import Optional

from helpers import TreeNode, bfs_print, binary_tree


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        mins = [float("inf")]

        def dfs(node, mins, rootval):
            if not node:
                return -1

            if node.val < mins[0] and node.val and node.val != rootval:
                mins[0] = node.val

            dfs(node.left, mins, root.val)
            dfs(node.right, mins, root.val)

        dfs(root, mins, root.val)

        if mins[0] < float("inf"):
            return int(mins[0])
        else:
            return -1
