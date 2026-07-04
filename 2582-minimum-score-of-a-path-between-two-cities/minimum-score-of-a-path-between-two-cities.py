class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # Build the adjacency list graph
        # graph[u] will store tuples of (v, distance)
        graph = collections.defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        # Initialize BFS variables
        min_score = math.inf
        queue = collections.deque([1])
        visited = {1}
        
        while queue:
            curr_city = queue.popleft()
            
            for neighbor, distance in graph[curr_city]:
                # Update our answer with every edge weight encountered in this component
                min_score = min(min_score, distance)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score