"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.



Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.


Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
"""

from typing import List


def arrayPairSum(nums: List[int]) -> int:
    # initialize result
    result = 0

    # start by sorting the pair by reverse order (so the highest numbers are paired together and can be added to the final sum)
    nums = sorted(nums)[::-1]

    # loop to get all the pairs
    for i in range(0, len(nums), 2):
        result += min(nums[i], nums[i + 1])

    return result


def bucket_solution(nums: List[int]) -> int:
    """Bucket sort solution -> bucket sort allow O(n) sorting, which show a big imporovment compare to the O(nlogn) method from the classic sort.
    We do need to take into consideration the range of the list to set up correctly the bucket.

    Args:
        nums (List[int]): list of numbers

    Returns:
        int: the result
    """
    # initialize result:
    result = 0
    bucket = [0] * 20000

    # Sort by using a bucket count (take down from -10000 up to 10000 numbers)
    for num in nums:
        bucket[num + 10000] += 1

    # Initialize the flag to true (to know when to pick up the number -> 1 / 2 )
    flag = True
    # Iterate through the bucket and add each 2 numbers (the minimum one)
    for i in range(len(bucket)):
        while bucket[i]:
            # add the number to the result if flagged
            if flag:
                result += i - 10_000

            # substract 1 number count
            bucket[i] -= 1

            # reverse the flag
            flag = not flag

    return result


if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print("Sort method: ", arrayPairSum(nums=nums))
    print("Bucket method: ", bucket_solution(nums=nums))

    nums = [6, 2, 6, 5, 1, 2]
    print("Sort method: ", arrayPairSum(nums=nums))
    print("Bucket method: ", bucket_solution(nums=nums))
