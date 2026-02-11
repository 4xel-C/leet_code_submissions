"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
"""

from typing import List


class Solution:
    """Strategie: Will monitor the smallest rectangle always incremented in order to count the numbers of maximums."""

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row = m
        col = n

        for op_row, op_col in ops:
            row = min(op_row, row)
            col = min(op_col, col)

        return row * col
