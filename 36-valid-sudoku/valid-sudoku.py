class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    # Create unique identifiers for row, column, and 3x3 box
                    # Use tuple or string to store in set
                    row_key = (r, "row", val)
                    col_key = ("col", c, val)
                    box_key = ("box", r // 3, c // 3, val)
                    
                    # If any key is already in the set, the board is invalid
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    
                    # Add keys to the set
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
                    
        return True