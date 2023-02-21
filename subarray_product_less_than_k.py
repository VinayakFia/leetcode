from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        cur_mul = 1
        lo = 0
        hi = 0
        
        while lo < len(nums):
            if hi == len(nums):
                cur_mul /= nums[lo]
                lo += 1
                
                if cur_mul < k:
                    res += 1
                    print(lo, hi)
            else:                
                n = nums[hi]
                
                if cur_mul * n < k:
                    res += 1
                    hi += 1
                    cur_mul *= n
                    print(lo, hi)
                else:
                    lo += 1
                    cur_mul /= n
        
        return res
    
print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))