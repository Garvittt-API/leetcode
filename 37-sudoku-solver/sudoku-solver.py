class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Pre-fill sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val in '123456789':
                            b_idx = (r // 3) * 3 + (c // 3)
                            if val not in rows[r] and val not in cols[c] and val not in boxes[b_idx]:
                                # Place
                                board[r][c] = val
                                rows[r].add(val)
                                cols[c].add(val)
                                boxes[b_idx].add(val)
                                
                                if solve(): return True
                                
                                # Backtrack
                                board[r][c] = '.'
                                rows[r].remove(val)
                                cols[c].remove(val)
                                boxes[b_idx].remove(val)
                        return False
            return True

        solve()