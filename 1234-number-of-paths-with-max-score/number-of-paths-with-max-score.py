class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 1_000_000_007
        n = len(board)
        
        # Keep the 2D grid to preserve state clarity, but keep the loop unrolled
        dp = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]
        
        # Base Case: Top-left cell 'E'
        dp[0][0] = 0
        count[0][0] = 1
        
        for i in range(n):
            for j in range(n):
                if (i == 0 and j == 0) or board[i][j] == 'X':
                    continue
                
                max_score = -1
                path_count = 0
                
                # 1. Look UP (i-1, j)
                if i > 0 and dp[i - 1][j] != -1:
                    max_score = dp[i - 1][j]
                    path_count = count[i - 1][j]
                
                # 2. Look LEFT (i, j-1)
                if j > 0 and dp[i][j - 1] != -1:
                    if dp[i][j - 1] > max_score:
                        max_score = dp[i][j - 1]
                        path_count = count[i][j - 1]
                    elif dp[i][j - 1] == max_score:
                        path_count = (path_count + count[i][j - 1]) % MOD
                
                # 3. Look UP-LEFT DIAGONAL (i-1, j-1)
                if i > 0 and j > 0 and dp[i - 1][j - 1] != -1:
                    if dp[i - 1][j - 1] > max_score:
                        max_score = dp[i - 1][j - 1]
                        path_count = count[i - 1][j - 1]
                    elif dp[i - 1][j - 1] == max_score:
                        path_count = (path_count + count[i - 1][j - 1]) % MOD
                
                # If reachable, append current cell's value
                if max_score != -1:
                    val = board[i][j]
                    current_val = int(val) if val != 'S' else 0
                    dp[i][j] = max_score + current_val
                    count[i][j] = path_count
                    
        if dp[n - 1][n - 1] == -1:
            return [0, 0]
        return [dp[n - 1][n - 1], count[n - 1][n - 1]]