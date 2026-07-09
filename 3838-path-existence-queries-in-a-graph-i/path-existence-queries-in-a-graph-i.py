class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # group[i] will store the ID of the connected component node i belongs to
        group = [0] * n
        component_id = 0
        
        # Identify the contiguous connected components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1
            group[i] = component_id
            
        # Answer each query instantly by comparing component IDs
        return [group[u] == group[v] for u, v in queries]