"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]

        # Keep the index of the row and cols
        top = 0
        bot = n - 1
        left = 0
        right = n - 1

        # Track the number to add
        k = 1

        while left <= right and bot >= top:
            # Fill up the first row
            for col in range(left, right + 1):
                result[top][col] = k
                k += 1

            # update the top row
            top += 1

            # Fill up the right column
            for row in range(top, bot + 1):
                result[row][right] = k
                k += 1

            # update the right column
            right -= 1

            # Fill up the bottom line (reverse)
            for col in range(right, left - 1, -1):
                result[bot][col] = k
                k += 1

            # update the bottom row pointer
            bot -= 1

            # Fill up the left line, reversed order
            for row in range(bot, top - 1, -1):
                result[row][left] = k
                k += 1

            # update the left row
            left += 1

        return result


if __name__ == "__main__":
    solver = Solution()

    n = 3
    print(solver.generateMatrix(n))
