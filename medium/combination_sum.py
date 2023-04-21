from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(); res = []
        def util(cur_sum: int, cur_candidates: List[int], last_added: int) -> None:
            if cur_sum == target: res.append(cur_candidates); return
            if cur_sum > target: return
            for n in candidates: 
                if n >= last_added: util(cur_sum + n, cur_candidates + [n], n)
        util(0, [], 0)
        return [*res]
    
print(Solution().combinationSum([2, 3, 6, 7], 7))