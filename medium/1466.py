from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[0]*n for i in range(n)]
        for c in connections: edges[c[0]][c[1]] = 1
        
        res = 0
        queue = [0]
        visited = [0 for i in range(n)]
        while len(queue) > 0:
            c = queue.pop(0)
            
            for i in range(n):
                if i == c: 
                    continue
                if edges[c][i] == 1 and visited[i] == 0:
                    res += 1
                    edges[c][i] = 0
                    edges[i][c] = 1
                    
            for i in range(n):
                if edges[i][c] == 1 and visited[i] == 0:
                    queue.append(i)
            
            visited[c] = 1
        
        return res
    
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
        