class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Pre-allocate array for fast localized cache lookups
        group = [0] * n
        curr = 0
        
        # Using a zipped loop is faster in Python than range indexing
        for i, (prev_val, curr_val) in enumerate(zip(nums, nums[1:]), 1):
            if curr_val - prev_val > maxDiff:
                curr += 1
            group[i] = curr
            
        # Localize the array lookup to speed up the list comprehension
        return [group[u] == group[v] for u, v in queries]