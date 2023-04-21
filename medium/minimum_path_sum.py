from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        dp = [[0] * n for i in range(m)]; dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0: continue
                val = 101
                if row - 1 >= 0: val = min(dp[row - 1][col], val)
                if col - 1 >= 0: val = min(dp[row][col - 1], val)
                dp[row][col] = grid[row][col] + val
        return dp[m - 1][n - 1]
    
print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))