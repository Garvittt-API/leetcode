class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Sort elements and track original indices
        sorted_pairs = sorted([(val, i) for i, val in enumerate(nums)])
        
        # Fast array allocation
        pos = [0] * n
        for sorted_idx, (_, orig_idx) in enumerate(sorted_pairs):
            pos[orig_idx] = sorted_idx
            
        # 2. 1-step max reach (Base case for binary lifting)
        far = [0] * n
        right = 0
        for left in range(n):
            # Move right pointer as far as valid
            while right < n and sorted_pairs[right][0] - sorted_pairs[left][0] <= maxDiff:
                right += 1
            far[left] = right - 1
            
        # 3. Cache-friendly Binary Lifting Table: st[LOG][n]
        st = [far]
        for _ in range(1, 18):
            prev = st[-1]
            # List comprehension runs at C-speed in Python
            st.append([prev[prev[i]] for i in range(n)])
            
        ans = []
        # Local variable lookup is faster in Python loops
        st_0 = st[0]
        
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
            
            # Greedily jump
            for j in range(17, -1, -1):
                if st[j][curr] < b:
                    curr = st[j][curr]
                    steps += (1 << j)
            
            # Final check using our cached 1-step array
            if st_0[curr] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans