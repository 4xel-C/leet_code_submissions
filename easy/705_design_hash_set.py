"""Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class: (Simple hashset implementation)

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]
"""

""" strategy: As we have a sontraint of 0 - 10^6 limit of the integers usable, I will simply use an array to access the information with a complexity of O(1).
On a real case, a limited array, alongside of a hash function (polynomial rolling hash ? SipHash? with modulus array length) should be considered, with a conflict resolving algorithm:
either using chained lilst for hash conflict, or open adresing (finding the closest open index in the array).
"""


class MyHashSet:
    def __init__(self):
        self.set = [False] * 1_000_001  # limit constraint given by the exercice

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key] is True
