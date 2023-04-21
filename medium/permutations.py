from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def util(cur):
            if len(cur) == len(nums): res.append(cur); return
            for n in nums: 
                if n not in cur: util(cur + [n])
        util([])
        return res