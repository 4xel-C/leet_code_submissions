"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: List[List[str]] = list()
        n_groups = 0

        groups: Dict[str, int] = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in groups:
                result[groups[sorted_word]].append(word)

            else:
                groups[sorted_word] = n_groups
                result.append([word])
                n_groups += 1

        return result


if __name__ == "__main__":
    solver = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(solver.groupAnagrams(strs))
