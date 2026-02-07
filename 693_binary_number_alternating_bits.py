"""Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.



Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """Apply XOR operation on twice shifted bits. Then check if have 0, 1 or any power of 2 number.
        To check if number is a power of two (only 1 bit), we can substract by 1 (all previous bits activated) and check that AND operation result to 0.
        """

        number = n ^ n // 4

        if number == 0 or number == 1 or (number & number - 1) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test = 5
    solution = Solution()
    print(solution.hasAlternatingBits(test))
