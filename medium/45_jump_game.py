"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Graph theory: we have a topological order, we can thus relax all edges to find the minimum (complexity O(V + E)). Consider each edge at weight 1"""

        # create the distance matrice to source
        dist = [float("inf") for _ in range(len(nums))]
        dist[0] = 0

        # relaxation loop
        for i, num in enumerate(nums):
            # Relax the edge of vertex i
            for j in range(1, num + 1):
                if i + j < len(nums):
                    dist[i + j] = min(dist[i] + 1, dist[i + j])
                    print(dist)

        return int(dist[len(nums) - 1])

    def jump_recursion(self, nums: List[int]) -> int:
        """Note: This solution is not optimal and will result in a time limit exceeded error for large inputs."""

        def _recursion(nums, start=0, jump_count=0) -> float:
            if start == len(nums) - 1:
                return jump_count

            jump_length = nums[start]

            result = float("inf")

            for i in range(1, jump_length + 1):
                if start + i < len(nums):
                    possible_jumps = _recursion(nums, start + i, jump_count + 1)
                    result = min(result, possible_jumps)

            return result

        return int(_recursion(nums))


if __name__ == "__main__":
    solver = Solution()
    nums = [
        5,
        6,
        4,
        4,
        6,
        9,
        4,
        4,
        7,
        4,
        4,
        8,
        2,
        6,
        8,
        1,
        5,
        9,
        6,
        5,
        2,
        7,
        9,
        7,
        9,
        6,
        9,
        4,
        1,
        6,
        8,
        8,
        4,
        4,
        2,
        0,
        3,
        8,
        5,
    ]
    print(solver.jump(nums))
