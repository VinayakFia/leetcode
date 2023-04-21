from cgitb import text


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        for c in text1:
            if c not in text2: 
                text1.replace(c, '')
        for c in text2:
            if c not in text1: 
                text2.replace(c, '')
        s1 = [*text1]
        s2 = [*text2]
        res = ""
        for i in range(min(text1, text2)):
            