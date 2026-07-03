class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(current_path):
            # Base case: if current path is same length as nums, we found a permutation
            if len(current_path) == len(nums):
                result.append(current_path[:])
                return
            
            for num in nums:
                # Skip if the number is already in the current path
                if num in current_path:
                    continue
                
                # Choose the number
                current_path.append(num)
                # Explore
                backtrack(current_path)
                # Un-choose (backtrack)
                current_path.pop()
                
        backtrack([])
        return result