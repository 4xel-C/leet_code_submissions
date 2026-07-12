"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

from typing import List


class Solution:
    """Strategy: pointer to the left, then to the right, and close the gap moving the smallet height first to seek for better values."""

    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        right = 0
        left = len(height) - 1

        while right < left:
            # Compute the area
            area = (left - right) * min(height[right], height[left])

            max_area = max(max_area, area)

            if height[right] <= height[left]:
                right += 1
            else:
                left -= 1

        return max_area


if __name__ == "__main__":
    solver = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(solver.maxArea(height))
