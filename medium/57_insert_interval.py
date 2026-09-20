"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        solution: list[list[int]] = list()

        if len(intervals) == 0:
            return [newInterval]

        # insert the interval in the current position
        inserted = False
        for i in range(len(intervals)):
            interval_lb = intervals[i][0]

            if interval_lb >= newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break

            if not inserted:
                intervals.append(newInterval)

        # Merge the intervals
        current_interval: list[int] = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            # Insert the current_interval normally
            if interval[0] <= current_interval[1]:
                # Merge if lower bound less than the upper bound
                current_interval[1] = max(current_interval[1], interval[1])

            else:
                solution.append(current_interval)
                current_interval = interval

        solution.append(current_interval)

        return solution


if __name__ == "__main__":
    solver = Solution()

    intervals = [[1, 5]]
    new_interval = [2, 7]

    print(solver.insert(intervals, new_interval))
