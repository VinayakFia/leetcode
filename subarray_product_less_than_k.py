from typing import List

# solutions too slow / wrong
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        cur_mul = 1
        lo = 0
        hi = 0
        
        while lo < len(nums) and hi < len(nums):              
            n = nums[hi]
            
            if cur_mul * n < k:
                print(lo, hi, nums[lo:hi + 1])
                res += 1
                cur_mul *= n

                if hi + 1 == len(nums) and not hi == lo:
                    cur_mul = 1
                    lo += 1
                    hi = lo
                else:
                    hi += 1
            else:
                lo += 1
                hi = lo
                cur_mul = 1
        
        return res
    
print(Solution().numSubarrayProductLessThanK([6,8,6,6,10,8,10,3,7,7,4,9,3,1], 121))