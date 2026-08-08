"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_sorted = sorted(candidates)
        result = list()

        def _backtrack(
            start: int = 0,
            current: List[int] = list(),
        ):
            if sum(current) == target:
                # copy to avoid mutability bug (list in result being updated)
                result.append(current[:])
                return

            elif sum(current) > target:
                return

            for i in range(start, len(candidates_sorted)):
                # avoid repeting combination if starting with the same numbers
                if (i != 0 and i != start) and candidates_sorted[
                    i
                ] == candidates_sorted[i - 1]:
                    continue

                current.append(candidates_sorted[i])
                _backtrack(i + 1, current)
                current.pop()

        _backtrack()

        return result


if __name__ == "__main__":
    solver = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print(solver.combinationSum2(candidates, target))
