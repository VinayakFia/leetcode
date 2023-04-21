class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid); n = len(grid[0])
        dp = [[0] * n for i in range(m)]
        visited = []

        def dfs(row: int, col: int) -> bool:
            nonlocal m, n

            if row >= m or row < 0:
                return True
            if col >= n or col < 0:
                return True
            if dp[row][col] == 1:
                return True
            if dp[row][col] == -1:
                return False
            if grid[row][col] == 0:
                return False
            if (row, col) in visited:
                return False
            
            visited.append((row, col))
            if dfs(row + 1, col):
                dp[row][col] = 1
            elif dfs(row - 1, col):
                dp[row][col] = 1
            elif dfs(row, col + 1):
                dp[row][col] = 1
            elif dfs(row, col - 1):
                dp[row][col] = 1
            else:
                dp[row][col] = -1

            return dp[row][col] == 1
        
        for i in range(m):
            for j in range(n):
                visited = []
                dfs(i, j)
                
        res = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    res += 1
        return res
            