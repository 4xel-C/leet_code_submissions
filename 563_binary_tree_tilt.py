"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Exemple 1:
Input: root = [1,2,3]
Output: 1
Explanation:
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1
"""

from typing import Optional

from helpers import TreeNode, build_tree_from_list


def findTilt(root: Optional[TreeNode]) -> int:
    def sumTree(node: Optional[TreeNode]) -> int:
        """Helper function to find the sum of all node in a tree"""
        if not node:
            return 0

        return node.val + sumTree(node.right) + sumTree(node.left)

    if not root:
        return 0

    def recursive_tilt(node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive implementation to compute the tilted values of a tree.
        """
        if not node:
            return None

        node.val = abs(sumTree(node.left) - sumTree(node.right))

        node.left = recursive_tilt(node.left)
        node.right = recursive_tilt(node.right)

        return node

    root = recursive_tilt(root)

    return sumTree(root)


if __name__ == "__main__":
    test_tree = build_tree_from_list([4, 2, 9, 3, 5, None, 7])

    print(findTilt(test_tree))
