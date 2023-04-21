from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lowestReach = len(nums) - 1
        dp = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            print(dp, dp[i+1:i+nums[i]+1])
            if nums[i] == 0: dp[i] = 10**4 + 1
            else: dp[i] = min(dp[i + 1:i + nums[i] + 1], default=0) + 1
        print(dp)
        return dp[0]

# [2,3,1,1,4]
# 0, 1, 2, 1, 2

print(Solution().canJump([2,0,2,4,6,0,0,3]))