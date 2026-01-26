"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].
"""

"""
Strategy: To solve this problem, we will start by sorting the array, then iterate on all the array keeping a cursor on the previous reference.
The difference between the cursor and the iteration variable will give the subsequence length
"""

from typing import List, Optional


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        sorted_list = sorted(nums)

        n = len(sorted_list)

        max_sub = 0

        cursor = 0

        for i in range(n):
            # If we a have a difference of more 1
            if sorted_list[i] - sorted_list[cursor] == 1:
                current_length = i + 1 - cursor
                max_sub = max(max_sub, current_length)

            elif sorted_list[i] - sorted_list[cursor] > 1:
                # update the cursor
                while sorted_list[i] - sorted_list[cursor] > 1:
                    cursor += 1

        return max_sub
