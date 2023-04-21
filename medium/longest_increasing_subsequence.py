from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        
        for i in range(len(nums)):
            if i == 0: 
                arr[i] = 1; 
                continue
            
            m = 0
            for j in range(i, -1, -1): 
                if nums[j] < nums[i] and arr[j] > m: 
                    m = arr[j]
                    
            arr[i] = m + 1
            
        return max(arr)
    
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
