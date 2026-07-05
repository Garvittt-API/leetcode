class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 1_000_000_007
        n = len(board)
        
        # dp[i][j] represents max score from (i, j) to (0, 0)
        dp = [[-1] * n for _ in range(n)]
        # count[i][j] represents number of paths achieving that max score
        count = [[0] * n for _ in range(n)]
        
        # Base Case: Top-left cell 'E'
        dp[0][0] = 0
        count[0][0] = 1
        
        # Process grid row by row, column by column
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X' or (i == 0 and j == 0):
                    continue
                
                # Check 3 incoming directions: up, left, up-left
                directions = [(i - 1, j), (i, j - 1), (i - 1, j - 1)]
                max_score = -1
                path_count = 0
                
                for prev_i, prev_j in directions:
                    if 0 <= prev_i < n and 0 <= prev_j < n and dp[prev_i][prev_j] != -1:
                        if dp[prev_i][prev_j] > max_score:
                            max_score = dp[prev_i][prev_j]
                            path_count = count[prev_i][prev_j]
                        elif dp[prev_i][prev_j] == max_score:
                            path_count = (path_count + count[prev_i][prev_j]) % MOD
                
                if max_score != -1:
                    current_val = int(board[i][j]) if board[i][j].isdigit() else 0
                    dp[i][j] = max_score + current_val
                    count[i][j] = path_count
        
        # Target result is at bottom-right corner 'S'
        if dp[n - 1][n - 1] == -1:
            return [0, 0]
        return [dp[n - 1][n - 1], count[n - 1][n - 1]]