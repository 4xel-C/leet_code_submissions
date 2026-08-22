"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        n = len(nums)

        def _recursion(
            result_list: List,
            n: int,
            nums=nums,
            current_permutation: List = list(),
        ):
            if len(current_permutation) == n:
                result_list.append(current_permutation.copy())
                return result_list

            for i, num in enumerate(nums):
                current_permutation.append(num)

                _recursion(
                    result_list,
                    n,
                    nums[:i] + nums[i + 1 :],
                    current_permutation,
                )

                # backtracking
                current_permutation.pop()

            return result_list

        return _recursion(result, n, nums, list())


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 2, 3]
    print(solver.permute(nums))
