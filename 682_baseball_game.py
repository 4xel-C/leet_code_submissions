"""You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.



Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

Example 2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
"""

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # number of operations
        n = len(operations)

        # global score
        total_score = list()

        for i in range(n):
            print(total_score)
            operation = operations[i]

            if operation == "+":
                total_score.append(total_score[-1] + total_score[-2])

            elif operation == "D":
                value = total_score[-1] * 2
                total_score.append(value)

            elif operation == "C":
                total_score.pop()

            else:
                total_score.append(int(operation))

        return sum(total_score)


if __name__ == "__main__":
    test = ["5", "2", "C", "D", "+"]
    test2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    solution = Solution()
    print(solution.calPoints(test2))
