"""Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # result list
        result = list()
        n = len(nums)

        # sort the list to detect the duplicated numbers
        nums.sort()

        # check permutation use backtrack, but continue the loop if the number is the same as the previous one
        def _recursion(result: List, nums: List[int], n: int, current: List = list()):
            # Base case: we have a permutation
            if len(current) == n:
                result.append(current.copy())
                return result

            # build the permutation
            for i, num in enumerate(nums):
                # Continue the loop if the previous number is the same than the current one to avoid duplicates
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                # update the current permutation
                current.append(num)

                # call the recursive function on the other possibilities
                _recursion(result, nums[:i] + nums[i + 1 :], n, current)

                # backtrack
                current.pop()

            return result

        return _recursion(result, nums, n)


if __name__ == "__main__":
    solver = Solution()
    test = [3, 3, 0, 3]
    print(solver.permuteUnique(test))
