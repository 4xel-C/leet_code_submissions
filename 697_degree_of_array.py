"""Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
"""

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        Strategy: Use a counting sort the iterate until finding the smallest degree, then get the numbers from which the degree is calculated.
        Finally: find the bounds in the main array encapsulating the degree (same numbers of maximum degree)
        Compute the minimum length of these subsets.
        """

        # Initialize the counting bucket
        bucket = [0] * 50_000
        first_occurence = [float("inf")] * 50_000
        last_occurence = [float("-inf")] * 50_000
        degree = 0

        for i, num in enumerate(nums):
            bucket[num] += 1
            first_occurence[num] = min(first_occurence[num], i)
            last_occurence[num] = max(last_occurence[i], i)
            degree = max(bucket[num], degree)

        result = float("inf")

        # iterate through the bucket to find the number and its bounds
        for num, num_degree in enumerate(bucket):
            # if we found a number with max degree, compute the left and right bounds
            if num_degree == degree:
                len_sublist = last_occurence[num] - first_occurence[num] + 1

                # update the result with the minimum length
                result = min(result, len_sublist)

        return int(result)


if __name__ == "__main__":
    test = [1, 2, 2, 3, 1]
    test2 = [1, 2, 2, 3, 1, 4, 2]
    sol = Solution()
    print(sol.findShortestSubArray(test2))
