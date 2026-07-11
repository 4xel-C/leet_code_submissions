"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    """Double pointer strategy: One on the starting substring, the other scanning the string:
    Save each seen character in a set, when duplicate, save the max length, and shift the head
    by poping each character inside until no dulicate remaining.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a set character observed so far
        char_set: set[str] = set()
        max_length = 0

        # initialize the pointers
        left = 0
        right = 0

        # Scan the string
        while right < len(s):
            char = s[right]

            while char in char_set:
                # Shift the left pointer while poping each of its seen letters
                char_set.remove(s[left])
                left += 1

            char_set.add(char)
            max_length = max(max_length, len(char_set))

            right += 1

        return max_length


if __name__ == "__main__":
    engine = Solution()
    test_s = "abcabcbb"
    print(engine.lengthOfLongestSubstring(test_s))
