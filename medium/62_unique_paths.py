"""
62. Unique Paths
Medium
Topics
premium lock icon
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
"""

from typing import List, Tuple


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Dynamic programming strategy: each cell possibilities equals the sum of the possibilities of the cell above + cell to the left"""

        # result matrix
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        # fill the first row
        for i in range(n):
            matrix[0][i] = 1

        # fill the left icolumn
        for i in range(m):
            matrix[i][0] = 1

        # fill the other cells
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]

    def uniquePathsRecursive(self, m: int, n: int) -> int:
        starting_pos: Tuple = (0, 0)

        # Possibles actions: r, d
        actions: List[Tuple] = [(1, 0), (0, 1)]

        result = [0]

        def _recursion(m: int, n: int, pos: Tuple[int, int]):
            x, y = pos

            # Base case: we found the bottom right corned
            if x == n - 1 and y == m - 1:
                result[0] += 1

            # recursively call the function
            for action in actions:
                next_x, next_y = x + action[0], y + action[1]

                # Sstay in the boundary of the state
                if next_x < 0 or next_x >= n:
                    continue
                elif next_y < 0 or next_y >= m:
                    continue

                _recursion(m, n, (next_x, next_y))

        _recursion(m, n, (0, 0))

        return result[0]


if __name__ == "__main__":
    solver = Solution()

    m = 3
    n = 7

    print(solver.uniquePaths(m, n))
