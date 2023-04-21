from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.res = {}

        def dfs(n: TreeNode) -> int:
            if n is None:
                return 0

            s = dfs(n.left) + dfs(n.right) + n.val

            if s in self.res:
                self.res[s] += 1
            else:
                self.res[s] = 1

            return s

        dfs(root)

        m = max(self.res.values())

        return [x for x in self.res if self.res[x] == m]
