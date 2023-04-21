from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = []
        atl = []
        m = len(heights)
        n = len(heights[0])
        def pacificAtlanticUtil(self, row: int, col: int, h) -> None:
            p = False; a = False
            if (col == 0 or row == 0) and [row, col] not in pac: pac.append([row, col]); p = True
            if (col == n or row == m) and [row, col] not in atl: atl.append([row, col]); a = True
            if a and p: return
            
            for y in range(row - 1, row + 2):
                for x in range(col - 1, col + 2):
                    if y >= m or y < 0 or x >= n or x < 0: continue
                    if [y, x] in pac and not p: pac.append([row, col]); p = True
                    if [y, x] in atl and not a: atl.append([row, col]); a = True
            