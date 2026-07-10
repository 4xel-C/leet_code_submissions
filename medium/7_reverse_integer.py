"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        # Convert into string and reverse the string
        num = str(x)

        if num.startswith("-"):
            result = int(num[0] + num[:0:-1])
        else:
            result = int(num[::-1])

        # Check if overflow
        if result > 2**31 - 1 or result < -(2**31):
            return 0

        else:
            return result


if __name__ == "__main__":
    test = Solution()

    print(test.reverse(-45))
