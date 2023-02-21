from typing import List


class Solution:
    closing = ")"
    opening = "("

    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        self.doGenerateParenthesis(n, "", res)
        return res

    def doGenerateParenthesis(self, n: int, s: str, res: List[str]) -> None:
        if len(s) == 2 * n:
            res.append(s)
            return

        if self.isValidParenthesis(n, s + self.opening):
            self.doGenerateParenthesis(n, s + self.opening, res)
        if self.isValidParenthesis(n, s + self.closing):
            self.doGenerateParenthesis(n, s + self.closing, res)
        
        return

    def isValidParenthesis(self, n: int, s: str) -> bool:
        if s.count(self.opening) > n or s.count(self.closing) > n:
            return False

        o = 0

        for c in s:
            if c == self.opening:
                o += 1
            else:
                o -= 1
            
            if o < 0:
                return False
        
        return True

solution: Solution = Solution()
print(solution.generateParenthesis(3))