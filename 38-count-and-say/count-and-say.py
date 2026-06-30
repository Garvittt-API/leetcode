class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            next_res = []
            length = len(res)
            i = 0
            while i < length:
                count = 1
                # Use a simple pointer scan to avoid list/iterator overhead
                while i + 1 < length and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                next_res.append(str(count))
                next_res.append(res[i])
                i += 1
            res = "".join(next_res)
        return res