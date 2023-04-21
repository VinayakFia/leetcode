class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp = []
        dp.append((nums[0], nums[0]))
        
        for i in range(1, len(nums)):
            n = nums[i]
            prev = dp[i-1]
            
            dp.append((
                max(n * prev[1], n * prev[0], n), 
                min(n * prev[1], n * prev[0], n)
            ))
            
        return max([max(x) for x in dp])
            
print(Solution().maxProduct([2,-5,-2,-4,3]))
            