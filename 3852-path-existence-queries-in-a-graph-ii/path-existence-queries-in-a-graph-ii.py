class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Sort elements and remember original indices
        sorted_pairs = sorted([(val, i) for i, val in enumerate(nums)])
        
        # pos[original_index] = new_sorted_index
        pos = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_pairs):
            pos[orig_idx] = sorted_idx
            
        LOG = 18
        # st[i][j] will store the farthest reachable index from i in 2^j steps
        st = [[0] * LOG for _ in range(n)]
        
        # 2. Compute 1-step max reach using Two Pointers
        right = 0
        for left in range(n):
            while right < n and sorted_pairs[right][0] - sorted_pairs[left][0] <= maxDiff:
                right += 1
            st[left][0] = right - 1
            
        # 3. Build Binary Lifting Table
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j-1]][j-1]
                
        ans = []
        
        # 4. Process queries
        for u, v in queries:
            a, b = pos[u], pos[v]
            
            if a > b:
                a, b = b, a
                
            if a == b:
                ans.append(0)
                continue
                
            curr = a
            steps = 0
            
            # Greedily jump as close to 'b' as possible WITHOUT reaching or passing it
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
            
            # Check if one more jump covers the remaining distance
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans