"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

from typing import Optional

from helpers import TreeNode, bfs_print, build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_equal(node: Optional[TreeNode], sub_node: Optional[TreeNode]) -> bool:
            """Helper method to check if a tree is equal to another tree."""

            if not node and not sub_node:
                return True
            elif not node or not sub_node:
                return False

            if node.val != sub_node.val:
                return False
            else:
                return all(
                    [
                        are_equal(node=node.left, sub_node=sub_node.left),
                        are_equal(node=node.right, sub_node=sub_node.right),
                    ]
                )

        def subtree_recursive(node, sub_root) -> bool:
            if not node:
                return False

            if are_equal(node, sub_root):
                return True

            return any(
                [
                    subtree_recursive(node.left, sub_root),
                    subtree_recursive(node.right, sub_root),
                ]
            )

        return subtree_recursive(root, subRoot)


if __name__ == "__main__":
    algo = Solution()
    root = build_tree_from_list([3, 4, 5, 1, 2])
    subroot = build_tree_from_list([4, 1, 2])

    print(algo.isSubtree(root, subroot))
    bfs_print(root)
