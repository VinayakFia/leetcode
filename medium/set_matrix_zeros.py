from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # find rows and cols that should be set to 0
        rows = set()
        cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0: rows.add(r); cols.add(c)
        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0 