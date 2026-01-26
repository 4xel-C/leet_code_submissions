"""
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
"""

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = len(list1)
        m = len(list2)

        common_string = list()
        common_string_index_sum = n + m

        for i in range(n):
            if i > common_string_index_sum:
                break

            for j in range(m):
                if (list1[i] == list2[j]) and (i + j) < common_string_index_sum:
                    # reinitialize the list as we found shorter substrring
                    common_string = list()
                    common_string.append(list1[i])
                    common_string_index_sum = i + j

                elif (list1[i] == list2[j]) and (i + j) == common_string_index_sum:
                    common_string.append(list1[i])

        return common_string
