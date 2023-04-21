from typing import List


# O(~1.63n)
class Solution:
    def longestCycle(self, out: List[int]) -> int:
        n = len(out)
        self.inn = {x: [] for x in range(n)}
        self.res = -1
        self.path = {}

        for i in range(n):
            if out[i] != -1:
                self.inn[out[i]].append(i)

        def dfs(c: int, l: int) -> None:
            if len(self.inn[i]) == 0 or c == -1:
                return
            if c in self.path and self.path[c] == -1:
                return
            if c in self.path:
                self.res = max(self.res, l - self.path[c])
                return

            self.path[c] = l
            dfs(out[c], l + 1)
            self.path[c] = -1
            return

        for i in range(n):
            dfs(i, 0)

        return self.res


print(Solution().longestCycle([1, 2, 1, 4, 2, 1, 3, 1, 6, 7, 4, 3, 2, 4, 5, 1, 3, 5, 2, 2]]))
