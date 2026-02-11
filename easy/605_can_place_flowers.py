"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowers_remaining = n

        length = len(flowerbed)

        # iterate through the array
        for i in range(length):
            if not flowerbed[i]:
                # check left and right
                if (i == 0 or not flowerbed[i - 1]) and (
                    i == (length - 1) or not flowerbed[i + 1]
                ):
                    flowerbed[i] = 1
                    flowers_remaining -= 1

                    if flowers_remaining == 0:
                        return True

        return False
