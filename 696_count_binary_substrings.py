"""Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.



Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """Count the consecutive number, then find the minimum  of consecutive length."""

        # separe the 0 and 1 chunks
        s = s.replace("01", "0 1").replace("10", "1 0")
        chunks = s.split(" ")

        chunks_len = list(map(lambda x: len(x), chunks))

        # get the minimum between two adjacent values
        zipped_len = zip(chunks_len[:-1], chunks_len[1:])

        result = 0

        for len1, len2 in zipped_len:
            result += min(len1, len2)

        return result


if __name__ == "__main__":
    test = "00110001110"

    solution = Solution()
    print(solution.countBinarySubstrings(test))
