from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        dp = [[0] * n for i in range(m)]; dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row > 0 and col > 0: dp[row][col] = min(dp[row-1][col] + grid[row][col], dp[row][col-1] + grid[row][col])
                elif row > 0: dp[row][col] = dp[row-1][col] + grid[row][col]
                elif col > 0: dp[row][col] = dp[row][col-1] + grid[row][col]
        return dp[m - 1][n - 1]