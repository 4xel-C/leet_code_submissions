"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


class Solution:
    """Strategy: use 3 pointers right, left and middle on a sorted array to efficiently find the sums"""

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)

        result: list[list] = list()

        for i in range(len(sorted_nums) - 1):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if total == 0:
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

                    j += 1

                    while sorted_nums[j] == sorted_nums[j - 1] and j < k:
                        j += 1

                # if total less than 0, move j to the right as we want to increase the sum
                elif total < 0:
                    j += 1

                # Decrease the sum (move k top the left)
                elif total > 0:
                    k -= 1

        return result


if __name__ == "__main__":
    nums = [0, 0, 0, 0]

    solver = Solution()
    print(solver.threeSum(nums))
