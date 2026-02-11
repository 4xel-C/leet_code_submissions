"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        original_r = len(mat)
        original_c = len(mat[0])

        n = original_r * original_c

        if (n != r * c) or (original_r == r and original_c == c):
            return mat

        # matrix initialisation
        reshaped_matrix = [[0 for col in range(c)] for row in range(r)]

        cursor_r = 0
        cursor_c = 0

        for row in mat:
            for num in row:
                reshaped_matrix[cursor_r][cursor_c] = num
                cursor_c += 1

                if cursor_c % c == 0:
                    cursor_c = 0
                    cursor_r += 1

        return reshaped_matrix


if __name__ == "__main__":
    test = Solution()

    mat = [[1, 2], [3, 4]]

    new_matrix = test.matrixReshape(mat, r=4, c=1)

    print("Original matrix: ", mat)
    print("New matrix: ", new_matrix)
