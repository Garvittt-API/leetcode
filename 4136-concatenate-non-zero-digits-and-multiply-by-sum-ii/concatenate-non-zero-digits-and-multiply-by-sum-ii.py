class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        # Local variable lookups are faster in Python functions
        MOD = 1000000007
        n = len(s)
        
        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        curr_pow = 1
        for i in range(1, n + 1):
            curr_pow = (curr_pow * 10) % MOD
            pow10[i] = curr_pow
            
        sum_d = [0] * (n + 1)
        cnt_n0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        # Micro-optimization: avoid int(char) by using ASCII values
        # ord('0') is 48
        curr_sum = 0
        curr_n0 = 0
        curr_p = 0
        
        for i, char in enumerate(s, 1):
            d = ord(char) - 48
            curr_sum += d
            sum_d[i] = curr_sum
            
            if d > 0:
                curr_n0 += 1
                curr_p = (curr_p * 10 + d) % MOD
            
            cnt_n0[i] = curr_n0
            p[i] = curr_p

        # Pre-allocate the result array to avoid dynamic resizing via .append()
        ans = [0] * len(queries)
        
        for i, (l, r) in enumerate(queries):
            n0 = cnt_n0[r + 1] - cnt_n0[l]
            sd = sum_d[r + 1] - sum_d[l]
            
            # Fast subtraction instead of general modulo for handling negative numbers
            # (p[l] * pow10[n0]) % MOD can be greater than p[r + 1]
            sub = (p[l] * pow10[n0]) % MOD
            x = p[r + 1] - sub
            if x < 0:
                x += MOD
                
            ans[i] = (x * sd) % MOD
            
        return ans