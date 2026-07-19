"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # keep a list of the momeory addressesi in order
        nodes = list()

        pointer = head

        while pointer:
            nodes.insert(0, pointer)
            pointer = pointer.next

        if n == len(nodes) and n == 1:
            head = None
        
        elif n == len(nodes):
            head = nodes[n - 2]
        
        elif n == 1:
            nodes[n].next = None
        
        else:
            nodes[n].next = nodes[n-2]
        
        return head





        if n > 0:
            nodes[n+1].next = nodes[n-1]
        if n == len(nodes) - 1:
            head = nodes[n]
        elif n > 0:
            nodes[n+1].next = nodes[n-1]
        
        else:
            nodes[n+1].next = None
        
        return head



if __name__ == "__main__":
    ..
