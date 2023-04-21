from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * amount; dp[0] = 0
        for i in range(1, amount):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[-1] if dp[-1] == (amount + 1) else -1            

print(Solution().coinChange([186,419,83,408], 6249))