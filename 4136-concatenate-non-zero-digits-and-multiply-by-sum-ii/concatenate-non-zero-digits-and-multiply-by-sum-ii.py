class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        sum_d = [0] * (n + 1)
        cnt_n0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        for i, char in enumerate(s, 1):
            d = int(char)
            sum_d[i] = sum_d[i - 1] + d
            cnt_n0[i] = cnt_n0[i - 1] + (1 if d > 0 else 0)
            p[i] = (p[i - 1] * 10 + d) % MOD if d > 0 else p[i - 1]
            
        ans = []
        for l, r in queries:
            n0 = cnt_n0[r + 1] - cnt_n0[l]
            sd = sum_d[r + 1] - sum_d[l]
            
            # Extract x using the prefix rule
            x = (p[r + 1] - p[l] * pow10[n0]) % MOD
            ans.append((x * sd) % MOD)
            
        return ans