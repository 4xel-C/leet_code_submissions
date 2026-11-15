"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        col_zeroes = set()
        row_zeroes = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_zeroes.add(i)
                    col_zeroes.add(j)

        # set the row to zeroes:
        for i in row_zeroes:
            matrix[i] = [0] * m

        # set the column to zeroes:
        for i in range(n):
            for idx in col_zeroes:
                matrix[i][idx] = 0


if __name__ == "__main__":
    solver = Solution()
