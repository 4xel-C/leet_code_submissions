"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

from typing import List


class Solution:
    """Strategy: recursive addition of the members of the sorted list increasingly the number until it get higher than the target."""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _recursion(
            solution: List[List[int]],
            candidates: List[int],
            target: int,
            current_combination: List[int] = list(),
            current_idx: int = 0,
        ):
            # Calculate the actual sum
            actual_sum = sum(current_combination)

            # Base cases: either we reach the target, or we go beyond
            if actual_sum == target:
                solution.append(current_combination)
                return

            # If we go beyond the number, prune the recursive current level
            elif actual_sum > target:
                return

            # sum with the current idx and all othert potential candidates
            for idx in range(current_idx, len(candidates)):
                _recursion(
                    solution,
                    candidates,
                    target,
                    current_combination + [candidates[idx]],
                    idx,
                )

        # Sort the list
        sorted_candidates = sorted(candidates)

        # instantiate the solution list
        solution = list()

        # start on each candidates
        _recursion(
            solution,
            sorted_candidates,
            target,
            current_idx=0,
        )

        return solution


if __name__ == "__main__":
    solver = Solution()

    candidates = [3, 5, 8]
    target = 11

    print(solver.combinationSum(candidates, target))
