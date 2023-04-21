from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count

        """
        switched = True
        i = len(nums)
        while switched == True:
            switched = False
            l = 0
            r = 1
            while r < i:
                if nums[l] == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    switched = True
                l += 1
                r += 1
            i -= 1
        """
                
print(Solution().moveZeroes([0,1,0,3,12]))