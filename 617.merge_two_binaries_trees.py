"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

from typing import Optional

from helpers.binary_tree import TreeNode, bfs_print, build_tree_from_list


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1

        def _recursive_merge_node(node1, node2) -> Optional[TreeNode]:
            if not node1 and not node2:
                return None
            elif not node1:
                return node2
            elif not node2:
                return node1

            merged_node = TreeNode(node1.val + node2.val)

            merged_node.left = _recursive_merge_node(node1.left, node2.left)
            merged_node.right = _recursive_merge_node(node1.right, node2.right)

            return merged_node

        return _recursive_merge_node(root1, root2)


if __name__ == "__main__":
    test1 = build_tree_from_list([1, 3, 2, 5])
    test2 = build_tree_from_list([2, 1, 3, None, 4, None, 7])

    solution = Solution()

    bfs_print(solution.mergeTrees(test1, test2))
