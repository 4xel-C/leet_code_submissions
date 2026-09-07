"""Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    """Strategy: Add the first line of the matrix to the reslut list, pop the row, then rotate the matrix. Repeat until the list is empty."""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()

        while len(matrix) > 0:
            for num in matrix[0]:
                result.append(num)

            matrix.pop(0)
            if len(matrix) == 0:
                break
            matrix = self.rotate_matrix(matrix)

        return result

    def rotate_matrix(self, matrix: List[List[int]]):
        transposed_matrix = self.transpose(matrix)

        rotated_matrix = list()

        for row in transposed_matrix[::-1]:
            rotated_matrix.append(row)

        return rotated_matrix

    def transpose(self, matrix: List[List[int]]):
        transposed_matrix = [list() for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed_matrix[j].append(matrix[i][j])

        return transposed_matrix


if __name__ == "__main__":
    solver = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    # transpose the marix
    print(solver.spiralOrder(matrix))
