"""Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = max_sum = nums[0]

        for num in nums[1:]:
            if current < 0:
                current = num
            else:
                current += num

            max_sum = max(current, max_sum)

        return max_sum

    def maxSubArrayErroneous(self, nums: List[int]) -> int:
        # Start from both end then reduce progressivly as a greedy algorithm (either left or right)
        left = 0
        right = len(nums) - 1

        max_sum = sum(nums)

        while left < right:
            print("current array: ", nums[left : right + 1])
            i = left
            j = right

            if nums[left] == nums[right]:
                while i < j and nums[i] == nums[j]:
                    i += 1
                    j -= 1

                    if nums[i] < nums[j]:
                        left = i

                    elif nums[i] > nums[j]:
                        right = j

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

            max_sum = max(max_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]

    print(solver.maxSubArray(nums))
