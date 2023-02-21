from math import ceil, floor


class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        
        l = 1
        r = x
        res = 0
        
        while l <= r:
            c = round((l + r) / 2)
            if x < c ** 2:
                r = c - 1
            elif x > c ** 2:
                l = c + 1
                res = c
            else:
                return c
        
        return res
        
            
print(Solution().mySqrt(8))