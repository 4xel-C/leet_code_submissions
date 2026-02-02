"""Helper file to build a tree from a list: follow Breadth Frist order"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def build_tree_from_list(values: List[Optional[int]]) -> TreeNode:
    # initialize the tree root
    root = TreeNode()

    # Copy the input list in a queue structure.
    values_to_insert = deque(values)

    root_value = values_to_insert.popleft()

    if root_value is None:
        raise ValueError("The tree needs at least a root value!")

    root.val = root_value

    # queue for bfs traversal
    queue_nodes = deque([root])

    while values_to_insert:
        val_left = None
        val_right = None

        # node to exepend
        node = queue_nodes.popleft()

        val_left = values_to_insert.popleft()

        if values_to_insert:
            val_right = values_to_insert.popleft()

        if val_left is not None:
            node.left = TreeNode(val=val_left)
            queue_nodes.append(node.left)

        if val_right is not None:
            node.right = TreeNode(val=val_right)
            queue_nodes.append(node.right)

    return root


def bfs_print(root: Optional[TreeNode]) -> None:
    if not root:
        return None

    stack_nodes: List[TreeNode] = [root]

    while stack_nodes:
        node = stack_nodes.pop(0)
        print(node.val)
        if node.left:
            stack_nodes.append(node.left)
        if node.right:
            stack_nodes.append(node.right)

    return


if __name__ == "__main__":
    test = [4, 2, 9, 3, 5, None, 7]

    tree = build_tree_from_list(test)
    bfs_print(tree)
