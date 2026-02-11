"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""

from typing import List

from helpers import Node


class Solution:
    def postorder(self, root: None) -> List[int]:
        if not root:
            return []

        result = []

        def postorder_recursive(node: Node, result_list: List):
            # recursive call on children
            if node.children:
                for child in node.children:
                    postorder_recursive(child, result_list)

            # Preorder R> append first the value before cascading to the children
            result_list.append(node.val)
            return

        # call the recursive function
        postorder_recursive(root, result)

        return result
