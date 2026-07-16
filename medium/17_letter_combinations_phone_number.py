"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def _backtrack(elements: List, idx: int = 0, combination="", result=list()):
            # If we reach the end of the groups to combine, append the combination and return the result
            if idx == len(elements):
                result.append(combination)
                return result

            # Get the current group to combine
            group = elements[idx]

            # Combine each letter of the group with the previous combination
            for letter in group:
                result = _backtrack(elements, idx + 1, combination + letter)

            return result

        elements = [phone_mapping[digit] for digit in digits]

        result = _backtrack(elements)

        return result


if __name__ == "__main__":
    solver = Solution()

    digits = "23"
    print(solver.letterCombinations(digits))
