from re import I
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        if n < 4: return max(nums[1], nums[0] + nums[1])
        arr = [nums[0], nums[1], nums[0] + nums[2]]       
        for i in range(3, n):
            arr.append(max(nums[i] + arr[i - 2], nums[i] + arr[i - 3]))
        print(arr)
        return max(arr)

print(Solution().rob([2,7,9,3,1]))
