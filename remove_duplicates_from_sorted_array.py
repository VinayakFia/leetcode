from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        
        for i in range(0, len(nums)):
            if nums[cur] == nums[i]:
                continue
            
            cur += 1
            nums[cur] = nums[i]
            
        print(cur)
        print(nums)
            
        return cur + 1
            
        
Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])