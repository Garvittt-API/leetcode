from typing import List
import sys

# Increase recursion depth just in case N is large
sys.setrecursionlimit(200000)

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Build adjacency list
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

        # Linear time check using DFS + Memoization (No Priority Queue!)
        def check(mid: int) -> bool:
            memo = {}
            
            def get_min_cost(u: int) -> int:
                if u == n - 1:
                    return 0
                if u in memo:
                    return memo[u]
                
                res = float('inf')
                for v, cost in adj[u]:
                    if cost >= mid: # Only traverse valid bottleneck edges
                        res = min(res, cost + get_min_cost(v))
                
                memo[u] = res
                return res
            
            return get_min_cost(0) <= k

        # Binary Search
        low, high = min_cost, max_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1  # Try to find a larger bottleneck
            else:
                high = mid - 1 # Tighten the bottleneck threshold
                
        return ans