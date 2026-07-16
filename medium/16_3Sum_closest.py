"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

from typing import List


class Solution:
    """Strategy: Use the 3 pointers (left, right, middle) on the sorted list number, iterate left for each num, and shift the right and the middle
    to get the closest possible of the target.
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        closest_sum = float("inf")

        for i in range(n - 1):
            left = i + 1
            right = n - 1

            # Check the closest 3 sums for this number
            while left < right:
                actual_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                # Check if we have a better sum
                if abs(target - actual_sum) < abs(target - closest_sum):
                    closest_sum = actual_sum

                # update the cursor to get closest to the sum
                if actual_sum < target:
                    # We want to increase the sum
                    left += 1
                else:
                    # We decrease the sum
                    right -= 1

        return int(closest_sum)


if __name__ == "__main__":
    solver = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(solver.threeSumClosest(nums, target))
