class Solution:
    def countAndSay(self, n: int) -> str:
        # Pre-defining strings for small counts to avoid repeated str() calls
        # This reduces overhead significantly
        counts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        res = "1"
        for _ in range(n - 1):
            next_res = []
            i = 0
            n_res = len(res)
            while i < n_res:
                char = res[i]
                count = 1
                while i + 1 < n_res and res[i + 1] == char:
                    count += 1
                    i += 1
                # Use the pre-defined counts and avoid str() function calls
                next_res.append(counts[count])
                next_res.append(char)
                i += 1
            res = "".join(next_res)
        return res