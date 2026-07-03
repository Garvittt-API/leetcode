class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        adj = [[] for _ in range(n)]
        min_cost = float('inf')
        max_cost = -1
        
        for u, v, cost in edges:
            if not online[u] or not online[v]:
                continue
            adj[u].append((v, cost))
            if cost < min_cost: min_cost = cost
            if cost > max_cost: max_cost = cost
            
        if max_cost == -1:
            return -1

        def check(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (total_cost, node)
            
            while pq:
                curr_cost, u = heappop(pq)
                
                if u == n - 1:
                    return curr_cost <= k
                if curr_cost > dist[u]:
                    continue
                if curr_cost > k:
                    break
                    
                for v, cost in adj[u]:
                    if cost < mid:
                        continue
                    next_cost = curr_cost + cost
                    if next_cost < dist[v]:
                        dist[v] = next_cost
                        heappush(pq, (next_cost, v))
                        
            return dist[n - 1] <= k

        low, high = min_cost, max_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans