"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create a set of jewels to ptimize the search
        jewels_set = {jewel for jewel in jewels}

        count: int = 0

        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbbbB"

    solver = Solution()

    print(solver.numJewelsInStones(jewels, stones))
