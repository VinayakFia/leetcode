from typing import List


class Solution:
    mem = []
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = []
        return self.wordBreakUtil(s, wordDict)

    def wordBreakUtil(self, r: str, wordDict: List[str]) -> bool:        
        self.mem.append(r)
        
        if len(r) == 0:
            return True
        
        for word in wordDict:
            if r[len(word):len(r)] in self.mem:
                continue
            
            if r.startswith(word):
                if self.wordBreakUtil(r[len(word):len(r)], wordDict):
                    return True
                
        return False
    
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
            