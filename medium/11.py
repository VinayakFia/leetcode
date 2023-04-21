class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums_sorted = sorted(nums)
        
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            
        
        print(nums)
        print(nums_sorted)
        
        return 0
    
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))