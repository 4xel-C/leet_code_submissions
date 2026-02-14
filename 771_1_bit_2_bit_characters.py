"""We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.



Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
"""

from typing import List


class Solution:
    """
    iterate through the aray, if 0 -> single character as two bytes character start with 1
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        i = 0

        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        # if i stop at the end of the array, the last bit is a one bit character, else, it's part of a two
        return i == n - 1
