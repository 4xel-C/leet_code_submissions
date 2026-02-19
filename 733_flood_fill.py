"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """Implementation by recursion

        Args:
            image (List[List[int]]): The image grid
            sr (int): The starting row
            sc (int): The starting column
            color (int): The color to change to

        Returns:
            List[List[int]]: The modified image
        """

        def recursive_flood(row, col, image, starting_color, new_color):
            """Modify recursivly the image in place"""

            # if no modification, return
            if starting_color == new_color:
                return

            if row < 0 or col < 0:
                return

            if row >= len(image) or col >= len(image[0]):
                return

            # Stop the recursion if the pixel is not from the starting color
            if image[row][col] != starting_color:
                return

            image[row][col] = new_color

            # extend to the neighbor
            recursive_flood(row - 1, col, image, starting_color, new_color)
            recursive_flood(row + 1, col, image, starting_color, new_color)
            recursive_flood(row, col - 1, image, starting_color, new_color)
            recursive_flood(row, col + 1, image, starting_color, new_color)

            return

        recursive_flood(sr, sc, image, image[sr][sc], color)

        return image
