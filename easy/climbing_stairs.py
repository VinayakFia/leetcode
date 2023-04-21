from math import comb, floor

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2] 
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[n - 1]
    
# [0, 1, 2, 2]
    
print(Solution().climbStairs(4))
