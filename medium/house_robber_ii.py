from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return max(nums)
        arr = [(nums[0], True), (nums[1], False)]       
        
        for i in range(2, n):
            print(arr)
            if i != n - 1:  
                if nums[i] + arr[i - 2][0] > nums[i] + arr[i - 3][0] or i == 2:
                    arr.append((nums[i] + arr[i - 2][0], arr[i - 2][1]))
                else:
                    arr.append((nums[i] + arr[i - 3][0], arr[i - 3][1]))
                continue
                        
            if not arr[i - 2][1] and not arr[i - 3][1]:
                arr.append(max((nums[i] + arr[i - 2][0], arr[i - 2][1]), 
                        (nums[i] + arr[i - 3][0], arr[i - 3][1])))
            elif not arr[i - 2][1] and arr[i - 3][1]:
                arr.append((nums[i] + arr[i - 2][0], False))
            elif not arr[i - 3][1] and arr[i - 2][1]:
                arr.append((nums[i] + arr[i - 3][0], False))
            else:
                arr.append((nums[i], True))
            
        print(arr)
        return max([x[0] for x in arr])
    
print(Solution().rob([1,2,3,1]))