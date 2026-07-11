"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Iterate over each list and rebuild the number in reverse order
        number1 = 0
        number2 = 0

        cursor1 = l1
        n1 = 0  # Number of elements in l1

        cursor2 = l2
        n2 = 0

        while cursor1:
            # Multiply by the exponent position not to use floats and divisions
            number1 += cursor1.val * 10**n1

            # keep track of the exponent position
            n1 += 1

            cursor1 = cursor1.next

        # same for second number
        while cursor2:
            number2 += cursor2.val * 10**n2

            # keep track of the number to regenerate the non floating number
            n2 += 1

            cursor2 = cursor2.next

        # result to insert
        result = number1 + number2

        # Insert the result in a reverse order in a new linked list
        # Keep the head of the list
        final_list = ListNode()
        cursor = final_list

        # While we still have nubmers to insert
        while result != 0:
            # Get the first number to insert
            value = result % 10

            # insert the value  and update the result to shift all numbers to the right
            cursor.val = value
            result //= 10

            # Create the next node if necessary
            if result != 0:
                cursor.next = ListNode()
                cursor = cursor.next

        return final_list
