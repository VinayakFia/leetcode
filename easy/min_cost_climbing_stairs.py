from tkinter import W
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [cost[0], cost[1]]
        n = len(cost)
        for i in range(2, n):
            arr.append(min(arr[i - 1] + cost[i], arr[i - 2] + cost[i]))
        return min(arr[n - 1], arr[n - 2])  
    
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))