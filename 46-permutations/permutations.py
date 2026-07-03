class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        visited = [False] * n
        
        def backtrack(current_path):
            if len(current_path) == n:
                result.append(current_path[:])
                return
            
            for i in range(n):
                if not visited[i]:
                    # Choose
                    visited[i] = True
                    current_path.append(nums[i])
                    
                    # Explore
                    backtrack(current_path)
                    
                    # Backtrack (Un-choose)
                    current_path.pop()
                    visited[i] = False
        
        backtrack([])
        return result