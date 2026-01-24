"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""

from typing import List

from helpers import Node, TreeNode, bfs_print, build_tree_from_list


class Solution:
    def preorder(self, root: None) -> List[int]:
        if not root:
            return []

        result = []

        def preorder_recursive(node: Node, result_list: List):
            # Preorder -> append first the value before cascading to the children
            result_list.append(node.val)

            # recursive call on children
            if node.children:
                for child in node.children:
                    preorder_recursive(child, result_list)

            return

        # call the recursive function
        preorder_recursive(root, result)

        return result
