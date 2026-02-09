"""You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
"""

from typing import Optional

from helpers import TreeNode, bfs_print, build_tree_from_list


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not node:
                return None

            if val == node.val:
                return node
            elif val < node.val:
                return search(node.left, val)
            else:
                return search(node.right, val)

        return search(root, val)
