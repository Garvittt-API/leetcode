class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        
        # Sort candidates to enable early termination (optimization)
        candidates.sort()
        
        def backtrack(remaining, start_index, path):
            if remaining == 0:
                # Found a valid combination
                results.append(list(path))
                return
            
            for i in range(start_index, len(candidates)):
                # If the candidate exceeds the remaining target, no need to continue
                if candidates[i] > remaining:
                    break
                
                # Include the candidate and recurse with the same index (unlimited usage)
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path)
                
                # Backtrack: remove the last added candidate to try the next one
                path.pop()
                
        backtrack(target, 0, [])
        return results