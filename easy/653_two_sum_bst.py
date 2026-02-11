"""Given the root of a binary search tree and an integer k, return true if there exist
two elements in the BST such that their sum is equal to k,
or false otherwise."""

from typing import Optional

from helpers import TreeNode, bfs_print, build_tree_from_list


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        unique_numbers = dict()

        number = k

        # Travel through the tree and add numbers to the set (BFS)
        # Initialize a queue
        queue = list()

        queue.append(root)

        # First traversal to store all the unique numbers
        while len(queue) > 0:
            # get the node
            node = queue.pop(0)

            if node is None:
                continue

            # Add the value to the set
            unique_numbers[node.val] = unique_numbers.get(node.val, 0) + 1

            # Extend the tree
            queue.append(node.left)
            queue.append(node.right)

        # Second traversal to find the difference
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)

            if node is None:
                continue

            # Check if it sums
            difference = number - node.val

            # discard 1 of the node.val count
            unique_numbers[node.val] -= 1

            # check if available in the set
            if difference in unique_numbers and unique_numbers[difference]:
                return True

            # restore the number in the dictionary
            unique_numbers[node.val] += 1

            queue.append(node.left)
            queue.append(node.right)

        return False
