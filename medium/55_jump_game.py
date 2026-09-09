"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        current = 0
        n = len(nums)

        while current < n and current <= max_reach:
            # Final case
            if max_reach >= n - 1:
                return True

            max_reach = max(max_reach, current + nums[current])
            current += 1

        return False

    def canJumpBFS(self, nums: List[int]) -> bool:
        """Employ BFS strategy to find the answer ?"""

        n = len(nums)

        # Base case
        if n == 1:
            return True

        queue = [0]

        while len(queue) > 0:
            # Deque first element in the list
            idx = queue.pop(0)

            # expand the current node for neighbors
            for i in range(1, nums[idx] + 1):
                neighbor = idx + i

                if neighbor >= n - 1:
                    return True

                # Add the neighbor to unexplored indices
                if neighbor not in queue:
                    queue.append(neighbor)

        return False


if __name__ == "__main__":
    solver = Solution()
    nums = [2, 0, 0]

    print(solver.canJump(nums))
