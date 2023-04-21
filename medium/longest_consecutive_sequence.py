from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = {}
        def util(n: int) -> int:
            if n not in nums: return 0
            if n in hashTable.keys(): return hashTable[n]
            hashTable[n] = util(n - 1) + 1
            return hashTable[n]
        best = 0
        for n in nums: 
            res = util(n)
            if res > best: best = res
        return best
    
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))    
        