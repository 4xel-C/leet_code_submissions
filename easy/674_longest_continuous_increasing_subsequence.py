"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].



Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
"""

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest_sub = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                current += 1
                longest_sub = max(current, longest_sub)

            else:
                longest_sub = max(current, longest_sub)
                current = 1

        return longest_sub
