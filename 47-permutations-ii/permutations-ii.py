class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path, used):
            # Base case: if the current path length matches nums, we found a permutation
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            for i in range(len(nums)):
                # Skip if the element is already used in the current path
                if used[i]:
                    continue
                    
                # Skip duplicates: if the current element is identical to the previous one,
                # and the previous one hasn't been used yet in this branch, skip it.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Make choice
                used[i] = True
                path.append(nums[i])
                
                # Recurse
                backtrack(path, used)
                
                # Undo choice (backtrack)
                path.pop()
                used[i] = False

        nums.sort()  # Essential for grouping duplicates together
        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result