"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 0
        cursorEnd = head

        # Get the length of the list and keep the last node
        while cursorEnd and cursorEnd.next:
            n += 1
            cursorEnd = cursorEnd.next
        n += 1

        if n in [0, 1] or k == 0:
            return head

        # compute the modulo to know the new head
        k = k % n

        # find the index of the last node of the rotated list
        index = n - k - 1
        cursor = head

        for _ in range(index):
            assert cursor and cursor.next is not None
            cursor = cursor.next

        # attach the end to the head of the list
        cursorEnd.next = head

        # define the new head
        head = cursor.next

        # detach the last node
        cursor.next = None

        return head

    def rotateRightModulo(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 0
        cursor = head

        # Get the length of the list
        while cursor:
            n += 1
            cursor = cursor.next

        if n in [0, 1] or k == 0:
            return head

        # compute the modulo to know the new head
        k = k % n

        # Rotate the list k times
        for i in range(k):
            cursor = head

            # get the node before the tail
            while cursor.next is not None and cursor.next.next is not None:
                print(cursor.val)
                cursor = cursor.next

            print(cursor.val)

            # Connect to the head
            cursor.next.next = head

            head = cursor.next

            cursor.next = None

        return head

    def rotateRightNaive(self, head: ListNode | None, k: int) -> ListNode | None:
        # Base case
        if head is None or head.next is None:
            return head


if __name__ == "__main__":
    solver = Solution()

    head = [0, 1, 2]
    k = 4

    solver.rotateRight(head, k)
