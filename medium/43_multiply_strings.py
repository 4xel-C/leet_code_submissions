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
        int1 = 0
        int2 = 0

        # rebuilt the numbers

        # Get the number 1 by one
        for char in num1:
            # shift the tens digit to the left
            int1 = int1 * 10

            # Add the new number
            num = ord(char) - 48
            int1 += num

        # Same for num2
        for char in num2:
            # shift the tens digit to the left
            int2 = int2 * 10

            # Add the new number
            num = ord(char) - 48
            int2 += num

        result = int1 * int2

        result_list = list()

        # convert the result into strings
        while result > 0:
            # get most right number
            digit = result % 10
            digit_char = chr(digit + 48)
            result_list.append(digit_char)

            # shift all the digit to the right
            result = result // 10

        # Concatenate the list to avod immutable string rebuilding on each iterations.
        # Reverse the list as the most right digit is at the beginning of the list.
        return "".join(result_list[::-1])


if __name__ == "__main__":
    solver = Solution()
    num1 = "3"
    num2 = "15"
    print(solver.multiply(num1, num2))
