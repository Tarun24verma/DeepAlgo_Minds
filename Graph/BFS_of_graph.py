from collections import deque
class Solution:
    def bfs(self, adj):
        # code here
        visited = [False] * (len(adj))
        q = deque()
        ans = []
        
        visited [0] = True
        q.append(0)
        
        while q:
            node = q.popleft()
            ans.append(node)
            
            for x in adj[node]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
        return ans