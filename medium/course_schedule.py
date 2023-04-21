from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses): adj[i] = []
        for edge in prerequisites: adj[edge[0]].append(edge[1])

        visited = set()

        def dfs(cur: int) -> bool:
            if cur in visited: return False
            if len(adj[cur]) == 0: return True
            
            visited.add(cur)
            for pre in adj[cur]:
                if not dfs(pre): return False
            visited.remove(cur)
            adj[cur] = []
            return True        

        for i in range(numCourses):
            if not dfs(i): return False
            
        return True
        
print(Solution().canFinish(2, [[1,0],[0,1]]))
