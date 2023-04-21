from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid); COLS = len(grid[0])
        visited = set()
        
        def dfs(row: int, col: int) -> List[Tuple[int]]:
            if row >= ROWS or row < 0 or col >= COLS or col < 0: return []
            if (row, col) in visited: return []
            if grid[row][col] == "0": return []
            
            visited.add((row, col))
            
            island = [(row, col)]
            island = island + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1)
            
            return island
        
        res = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                island = dfs(row, col)
                if len(island) != 0:
                    print(island)
                    res += 1
                    
        return res
