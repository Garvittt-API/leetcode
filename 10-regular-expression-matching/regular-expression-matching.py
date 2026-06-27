class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (match and dfs(i + 1, j))

            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)