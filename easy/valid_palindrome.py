class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        frmt_s = ""
        
        for char in s:
            if char.isalnum():
                frmt_s += char
            
        lo = 0
        hi = len(frmt_s) - 1
    
        while lo <= hi:
            if frmt_s[lo] != frmt_s[hi]:
                return False
            lo += 1
            hi -= 1
            
        return True
        