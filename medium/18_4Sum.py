"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


class Solution:
    """Strategy: Use 4 pointers on the sroted array: i, Start, left and right: for each start : solve the thre sum problem with the remaining numbers"""

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Base cases: return empty list
        if len(nums) < 4:
            return list()

        sorted_nums = sorted(nums)

        result = list()

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            for start in range(i + 1, len(sorted_nums) - 1):
                if start > i + 1 and sorted_nums[start] == sorted_nums[start - 1]:
                    continue

                left = start + 1
                right = len(sorted_nums) - 1

                while left < right:
                    actual_sum = (
                        sorted_nums[i]
                        + sorted_nums[start]
                        + sorted_nums[left]
                        + sorted_nums[right]
                    )

                    if actual_sum == target:
                        result.append(
                            [
                                sorted_nums[i],
                                sorted_nums[start],
                                sorted_nums[left],
                                sorted_nums[right],
                            ]
                        )
                        left += 1

                        while (
                            left < len(nums)
                            and sorted_nums[left - 1] == sorted_nums[left]
                        ):
                            left += 1

                    elif actual_sum < target:
                        left += 1

                        while (
                            left < len(nums)
                            and sorted_nums[left - 1] == sorted_nums[left]
                        ):
                            left += 1

                    elif actual_sum > target:
                        right -= 1

                        while (
                            right >= 0 and sorted_nums[right + 1] == sorted_nums[right]
                        ):
                            right -= 1

        return result


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    print(solver.fourSum(nums, target))
