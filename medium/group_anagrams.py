from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tables = []
        for s in strs:
            t = {}
            for c in s: t[c] = 0
            for c in s: t[c] += 1
            tables.append[t]
        for i in range(len(tables)):
            return
        
            