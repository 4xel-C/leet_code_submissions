"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Stratégie: We can find the total sum using sum = n*(n+1) / 2. If we compare with our actual sum we can deduce:
        actualsum = expectedsum - missing_number + duplicated_number
        <=>
        missing_number = expectedsum + duplicated_number - actualsum

        we can just focuss on duplicated number then.
        """
        if not nums:
            return list()

        n = len(nums)
        actualsum = sum(nums)
        expectedsum = (n * (n + 1)) / 2

        seen_numbers = set()

        for num in nums:
            if num in seen_numbers:
                missing_number = int(expectedsum + num - actualsum)
                return [num, missing_number]
            seen_numbers.add(num)

        # return empty list if all okay.
        return list()


if __name__ == "__main__":
    test = [1, 2, 2, 4]

    solution = Solution()

    print(solution.findErrorNums(test))
