"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """different strategy: Use power deocmposition, additive property, using the binary representation to decompose the power number"""

        if n == 0:
            return 1

        power = abs(n)
        result = 1
        current_power = x

        while power:
            # Using the binary representation of the power give the composition in product of power of power of 2
            if power & 1 == 1:
                result *= current_power

            # shift all bit by 1 unit to increase the power of 2
            current_power *= current_power
            power = power >> 1

        if n < 0:
            return 1 / result
        else:
            return result

    def myPowNaive(self, x: float, n: int) -> float:
        result = x

        # Keep track of the current power
        current_power = 0

        power = n * -1 if n < 0 else n

        if n == 0:
            return 1

        while current_power != power:
            if current_power < power:
                result = result * result
                current_power *= 2

        for i in range(power - 1):
            result = result * x

        if n < 0:
            return 1 / (result)
        else:
            return result


if __name__ == "__main__":
    solver = Solution()

    print("Test de 2^3 (assert = 8): ", solver.myPow(2, 3))

    print("Test de 2^-2 (assert = 0.25): ", solver.myPow(2, -2))

    print("Test de 2^10 (assert = 1042): ", solver.myPow(2, 10))
