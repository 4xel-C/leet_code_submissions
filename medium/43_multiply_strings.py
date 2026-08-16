"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


# TODO: Constraint violation : avoid computing multiplication on big int int1 * int 2. Strategy: compute multiplication digit per digit.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # list to store the result of the multiplication (reversed)
        result = ["" for _ in range(len(num1) + len(num2))]

        # muliply each number of number 1 with all numbers of numbers 2
        # Start from the end
        for i, char1 in enumerate(num1[::-1]):
            for j, char2 in enumerate(num2[::-1]):
                int1 = ord(char1) - 48
                int2 = ord(char2) - 48

                current_result = int1 * int2

                print(f"multiplying {int1} * {int2} = {current_result}")
                print(f"Position: {i + j + 1}")

                # store the result at the correct index adding to the current value
                counter = 0  # The counter to increment the index in case the current result contains 2 digits
                reminder = 0
                while current_result > 0 or counter == 0:
                    digit = (
                        (ord(result[i + j + counter]) - 48 + (current_result % 10))
                        if result[i + j + counter] != ""
                        else (current_result % 10)
                    )

                    print(f"Digit : {digit}")

                    if digit > 9:
                        reminder = 1
                        digit = digit % 10

                    result[i + j + counter] = str(digit)

                    print(result[::-1])

                    current_result //= 10
                    current_result += reminder
                    reminder = 0
                    counter += 1

        return "".join(result[::-1])


if __name__ == "__main__":
    solver = Solution()
    num1 = "6"
    num2 = "501"
    # result : 3006
    print(solver.multiply(num1, num2))
