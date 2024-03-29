from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for value in points:
            prev, curr = curr, max(prev + value, curr)
        return curr

print(Solution().deleteAndEarn([8,10,4,9,1,3,5,9,4,10]))
                