from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        cur_mul = 1
        lo = 0
        hi = 0
        
        while lo < len(nums) and hi < len(nums):              
            n = nums[hi]
            
            if cur_mul * n < k:
                print(lo, hi, "start")
                res += 1
                cur_mul *= n

                if hi + 1 == len(nums) and not hi == lo:
                    res += hi - lo + 1
                    break
                else:
                    hi += 1
            else:
                lo += 1
                hi = lo
                cur_mul = 1
        
        return res
    
print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))