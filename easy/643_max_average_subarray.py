"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Max average defined by the average of the maximum consecutive numbers of the list: track the max sum with a sliding window"""

        if k == 0:
            return 0
        elif k == 1:
            return max(nums)

        n = len(nums)

        # initialize with the sum of the first k numbers
        max_sum = sum(nums[:k])
        current_sum = max_sum

        for i in range(k, n):
            current_sum -= nums[i - k]
            current_sum += nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum / k


if __name__ == "__main__":
    k = 4
    nums = [1, 12, -5, -6, 50, 3]

    solution = Solution()

    print(solution.findMaxAverage(nums, k))
