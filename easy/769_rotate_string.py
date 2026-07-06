"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Base cases
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        # try each rotation
        for i in range(1, len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False
