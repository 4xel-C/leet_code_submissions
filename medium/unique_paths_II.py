"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Use dynamic programming to fill up the matrices of unique path numbers
        matrix_count = [
            [0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))
        ]

        # Fill the first line
        obstacle = False
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                obstacle = True
            matrix_count[0][i] = 1 if not obstacle else 0

        # fill the first column
        obstacle = False
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                obstacle = True
            matrix_count[i][0] = 1 if not obstacle else 0

        # solve the matrix count
        for row in range(1, len(matrix_count)):
            for col in range(1, len(matrix_count[0])):
                if obstacleGrid[row][col] == 1:
                    matrix_count[row][col] = 0
                else:
                    matrix_count[row][col] = (
                        matrix_count[row - 1][col] + matrix_count[row][col - 1]
                    )

        return matrix_count[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == "__main__":
    solver = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    print(solver.uniquePathsWithObstacles(obstacleGrid))
