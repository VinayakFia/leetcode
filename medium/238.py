class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # O(n) space complexity
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        if nums.count(0) == 1:
            mult = 1
            
            for x in nums:
                if x != 0:
                    mult *= x
                    
            return [0 if x != 0 else mult for x in nums]
        
        mult = 1
        for x in nums:
            mult *= x
                
        return [int(mult / x) for x in nums]