"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

from typing import List


class Solution:
    # Use binary search to find the number the starting position of the number, then the last position (2O(nlogn))
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        l_index = -1
        r_index = -1

        # binary search for left target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # check if it's left boundary
                if mid == 0 or nums[mid - 1] != target:
                    l_index = mid
                    break

                # If the target still on the previous index, continue the binary search
                if nums[mid - 1] == target:
                    right = mid - 1

            else:
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        # If no left boundary: no solution
        if l_index == -1:
            return [-1, -1]

        # second binary search for the other border
        left = 0
        right = len(nums)

        # binary search for left target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # check if it's right boundary
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    r_index = mid
                    break

                # If the target still on the previous next index, continue the binary search
                if nums[mid + 1] == target:
                    left = mid + 1

            else:
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return [l_index, r_index]
