class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Bitmasks for rows, columns, and 3x3 boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        def get_idx(r, c): return (r // 3) * 3 + (c // 3)

        # Pre-fill bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c]) - 1
                    mask = 1 << val
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[get_idx(r, c)] |= mask
                else:
                    empty.append((r, c))

        def get_possibilities(r, c):
            # Combined mask of used numbers in row, col, and box
            used = rows[r] | cols[c] | boxes[get_idx(r, c)]
            return ~used & 0x1FF  # All 1s for available spots

        def solve():
            if not empty: return True
            
            # Heuristic: Pick the cell with fewest possibilities
            best_idx = -1
            min_count = 10
            best_poss = 0
            
            for i, (r, c) in enumerate(empty):
                poss = get_possibilities(r, c)
                count = bin(poss).count('1')
                if count == 0: return False
                if count < min_count:
                    min_count = count
                    best_idx = i
                    best_poss = poss
                    if count == 1: break # Cannot do better than 1
            
            r, c = empty.pop(best_idx)
            for val in range(9):
                if (best_poss >> val) & 1:
                    mask = 1 << val
                    board[r][c] = str(val + 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[get_idx(r, c)] |= mask
                    
                    if solve(): return True
                    
                    # Backtrack
                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[get_idx(r, c)] &= ~mask
            
            empty.insert(best_idx, (r, c))
            return False

        solve()