"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        score_grid = [row[:] for row in grid]

        # use dynamic programming to compute the path

        # update the first column
        for row in range(1, len(score_grid)):
            score_grid[row][0] += score_grid[row - 1][0]

        # update the first line
        for col in range(1, len(score_grid[0])):
            score_grid[0][col] += score_grid[0][col - 1]

        # update the whole grid
        for row in range(1, len(score_grid)):
            for col in range(1, len(score_grid[0])):
                # Get the minimum cost to this cell: minimum of the path so far + the actual cost
                score_grid[row][col] = (
                    min(score_grid[row - 1][col], score_grid[row][col - 1])
                    + score_grid[row][col]
                )

        print(score_grid)
        return score_grid[len(score_grid) - 1][len(score_grid[0]) - 1]


if __name__ == "__main__":
    solver = Solution()
    grid = [[1, 2, 3], [4, 5, 6]]
    print(solver.minPathSum(grid))
