"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """STrategy: Check both end of the string until inequality: if different characters, check skipping one or another character."""

        def is_palindrome(s, start, end):
            """Internal function to check if is a palindrome"""
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1

            return True

        start = 0
        end = max(len(s) - 1, 0)

        while start < end:
            if s[start] != s[end]:
                return is_palindrome(s, start + 1, end) or is_palindrome(
                    s, start, end - 1
                )
            else:
                start += 1
                end -= 1

        return True


if __name__ == "__main__":
    s = "ecedec"

    solution = Solution()

    print(solution.validPalindrome(s))
