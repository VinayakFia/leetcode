from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        mx = nums[0]
        cr = 0

        crFlag = False
        
        while l != len(nums) and r < len(nums):
            if cr + nums[r] <= 0:
                l = r + 1
                cr = 0
            else:
                cr += nums[r]
                crFlag = True
                
            if cr > mx and crFlag:
                mx = cr 

            r += 1
        
        # if all elements in nums are negative
        if not crFlag:
            mx = max(nums)
            
        return mx
    
s: Solution = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))