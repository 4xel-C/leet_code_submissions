"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""

from typing import List, Optional


class Solution:
    def maximumProduct(self, nums: List[int]) -> Optional[int]:
        """Strategy used: tack the 2 min and 3 max numbers: compare the product of the 3 max, with the product with 1 max and 2 min
        as we want the highest values, so we should multiply 2 negatives numbers at most.
        """

        if len(nums) < 3:
            return None

        # track the 3 max numbers
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")

        # Track the 2 min numbers
        min1, min2 = float("inf"), float("inf")

        # iterate through the list and compute the numbers
        for num in nums:
            # if we have a new max, update all the value by cascading the max
            # above the total max
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num

            # above the medium max
            elif num >= max2:
                max3 = max2
                max2 = num

            # above the minmaximum
            elif num > max3:
                max1 = num

            # compute the minimum
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)  # type: ignore (at least 3 numbers, so they all will be updated).
