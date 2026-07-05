class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        # Lookups to check attacks in O(1) time
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        def backtrack(r):
            # Base case: All queens are successfully placed
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                # If the cell is under attack, skip it
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place the queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack: Remove the queen and try the next column
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res