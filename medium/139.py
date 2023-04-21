class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        mem = set()
        n = len(wordDict)
        
        def util(r: str, contains: list[str]) -> bool:
            nonlocal mem

            if r in mem:
                return False
            
            if len(r) == 0:
                return True
            
            for word in wordDict:
                if r.startswith(word):
                    if util(r[len(word):len(r)], contains + [word]):
                        return True
            
            mem.add(r)
                
            return False

        return util(s, [])
    
    
print(Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]))                
        