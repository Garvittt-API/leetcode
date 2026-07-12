class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Get sorted unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a map of value -> rank
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # Step 3: Map the original array to its ranks
        return [rank_map[num] for num in arr]