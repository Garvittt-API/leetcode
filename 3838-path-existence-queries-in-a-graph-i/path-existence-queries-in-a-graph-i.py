class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Localize EVERYTHING to eliminate scope resolution overhead
        g = [0] * n
        curr = 0
        
        # Pulling indexing mechanisms directly out of loops minimizes operations per step
        prev_v = nums[0]
        for i in range(1, n):
            curr_v = nums[i]
            if curr_v - prev_v > maxDiff:
                curr += 1
            g[i] = curr
            prev_v = curr_v
            
        # A fast list comprehension using local array 'g' 
        # avoids tuple unpacking or function call overhead
        return [g[q[0]] == g[q[1]] for q in queries]