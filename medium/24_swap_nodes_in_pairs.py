"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get a counter of index
        idx = 0

        # Keep the two previous node
        pv2: Optional[ListNode] = None
        pv1: Optional[ListNode] = None

        cursor = head

        while cursor is not None:
            # If the index is odd, swap with the previous
            if idx % 2 == 1:
                if pv1 is not None:
                    pv1.next = cursor.next
                    cursor.next = pv1

                    # If we have the starting node reversed, change the head.
                    if idx == 1:
                        head = cursor

                    if pv2 is not None:
                        pv2.next = cursor

                    # uupdate the previous (pv2 became cursor, and pv1 dosnt move)
                    pv2 = cursor
                    cursor = pv1

            # All the other cases: advance in the list
            else:
                if pv1 is not None:
                    pv1 = pv1.next
                else:
                    pv1 = cursor

                if pv2 is not None:
                    pv2 = pv2.next

            # go to next node
            cursor = cursor.next
            idx += 1

        return head
