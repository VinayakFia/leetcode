from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        path = set()
        visited = set()
        islands = []

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(c: int) -> None:
            if c in path or c in visited:
                return
            
            path.add(c)
            visited.add(c)
            for node in adj[c]:
                dfs(node)
                
            return
    
        for i in range(n):
            if i in visited: 
                continue
            path = set()
            dfs(i)
            islands.append(len(path))
        
        prefixSum = []
        prefixSum.append(sum(islands))
        for i in range(1, len(islands)):
            prefixSum.append(prefixSum[i - 1] - islands[i - 1])
            
        print(islands, prefixSum)
        
        res = 0
        for i in range(len(islands) - 1):
            res += islands[i] * prefixSum[i + 1]
        
        return res
    
print(Solution().countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))                     
            