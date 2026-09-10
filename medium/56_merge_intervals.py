"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Strategy: Filter by ascending order of lower bound, then scan the intervals to merge if
        the previous upper bound is > than the actual lower bound.

        Args:
            intervals (List[List[int]]): List of intervals

        Returns:
            List[List[int]]: List of merged intervals
        """
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        print(intervals)

        result: List[List[int]] = list()
        new_interval = intervals[0]

        for i in range(1, len(intervals)):
            if new_interval[1] >= intervals[i][0]:
                # Merge the intervals, consider englobing intervals
                new_interval = [
                    new_interval[0],
                    max(intervals[i][1], new_interval[1]),
                ]

            else:
                result.append(new_interval)
                new_interval = intervals[i]

            if i == len(intervals) - 1:
                result.append(new_interval)

        return result


if __name__ == "__main__":
    solver = Solution()
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

    print(solver.merge(intervals))
