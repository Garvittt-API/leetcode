class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        # Sort to handle duplicates and enable pruning
        candidates.sort()
        
        def backtrack(remaining, start_index, path):
            if remaining == 0:
                results.append(list(path))
                return
            
            for i in range(start_index, len(candidates)):
                # Skip duplicate candidates at the same level of the tree
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Pruning: if current candidate is too large, subsequent ones will be too
                if candidates[i] > remaining:
                    break
                
                # Include candidate, move to next index (i + 1) to ensure each is used once
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1, path)
                
                # Backtrack
                path.pop()
        
        backtrack(target, 0, [])
        return results