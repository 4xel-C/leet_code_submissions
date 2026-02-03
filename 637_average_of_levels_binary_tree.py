"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

exemple:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
"""

from typing import List, Optional

from helpers import TreeNode, bfs_print, build_tree_from_list


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """Strategie: BFS then compute mean of each level: for each search, calculate the means of all node in the queue, then extend them all"""

        queue_nodes = list()

        # result list of means of each level
        result_array = list()

        queue_nodes.append(root)

        while queue_nodes:
            level_nodes: List[TreeNode] = (
                queue_nodes.copy()
            )  # get all the node from the level
            queue_nodes: List = list()  # reset the list
            level_mean: float = 0
            n_level_nodes = 0

            for node in level_nodes:
                if not node:
                    continue

                level_mean += node.val
                n_level_nodes += 1

                # extend the node
                queue_nodes.append(node.left)
                queue_nodes.append(node.right)

            if n_level_nodes > 0:
                level_mean = level_mean / n_level_nodes
                result_array.append(level_mean)

        return result_array


if __name__ == "__main__":
    test = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    sol = Solution()
    print(sol.averageOfLevels(test))
