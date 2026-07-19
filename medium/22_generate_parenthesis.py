"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _backtrack(
            n: int, left_count: int = 0, combination="", result: list = list()
        ):
            # If we used all parenthesis, append the result and return
            if n == 0 and left_count == 0:
                result.append(combination)
                return result

            # Backtrack to add a left parenthesis
            if n > 0:
                _backtrack(n - 1, left_count + 1, combination + "(", result)

            # If the left count is > 0, we can close a parenthesis
            if left_count > 0:
                _backtrack(n, left_count - 1, combination + ")", result)

            return result

        return _backtrack(n)


if __name__ == "__main__":
    solver = Solution()

    print(solver.generateParenthesis(3))
