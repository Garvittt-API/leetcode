class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Pre-allocate array for fast, contiguous memory layout
        group = [0] * n
        curr = 0
        
        # Micro-optimization: standard for-loops with local vars are fastest for mutating elements
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr += 1
            group[i] = curr
            
        # Using map with a lambda bypasses the byte-code execution loop of a list comprehension,
        # executing the loop natively in C speed.
        return list(map(lambda q: group[q[0]] == group[q[1]], queries))