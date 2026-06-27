"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.



Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
"""

from typing import List


# TODO: take into consideration rectangular matrix
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        first_line = matrix[0]
        first_column = [matrix[0][0]]

        if len(matrix[0]) <= 1:
            return True

        for row in range(1, len(matrix)):
            # Add the first element of the row in the vectical line in first position for comparison
            first_column.insert(0, matrix[row][0])

            print(f"===Iteration {row}===")
            print("first line: ", first_line[:-row])
            print("compared with: ", matrix[row][row:])
            print("------")
            print("first column: ", first_column)
            print("compared with: ", matrix[row][: row + 1])

            if (
                matrix[row][row:] != first_line[:-row]
                or matrix[row][: row + 1] != first_column
            ):
                return False

        return True


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solver = Solution()

    print(solver.isToeplitzMatrix(matrix))
