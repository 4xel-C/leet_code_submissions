"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell
and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present,
we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        kernel_size = 3

        # initialize the result matrix
        result = [([0] * len(img[0])) for _ in img]

        for x in range(len(img)):
            for y in range(len(img[0])):
                cell_mean = list()

                # Get the values from the kernel
                for i in range(x - (kernel_size // 2), x + (kernel_size // 2) + 1):
                    for j in range(y - (kernel_size // 2), y + kernel_size // 2 + 1):
                        if i < 0 or j < 0 or i >= len(img) or j >= len(img[0]):
                            continue

                        cell_mean.append(img[i][j])

                cell_mean = sum(cell_mean) / len(cell_mean) if len(cell_mean) > 0 else 0

                result[x][y] = int(cell_mean)

        return result
