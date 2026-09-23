import time
import copy

original_grid = [
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 8, 1, 0, 5, 0, 4, 0, 0],
    [0, 0, 9, 0, 0, 7, 0, 5, 8],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 1, 0, 0, 7],
    [7, 4, 0, 0, 0, 0, 2, 0, 1],
    [0, 0, 0, 1, 3, 0, 0, 0, 4],
    [0, 0, 0, 0, 2, 9, 0, 0, 0],
    [9, 0, 0, 0, 0, 8, 0, 6, 0]
]
def is_valid(board, r, c, val):
    for i in range(9):
        if board[r][i] == val or board[i][c] == val:
            return False
        if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
            return False
    return True
calls_seq = 0
def solve_seq(board):
    global calls_seq
    calls_seq += 1
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for val in range(1, 10):
                    if is_valid(board, r, c, val):
                        board[r][c] = val
                        if solve_seq(board): return True
                        board[r][c] = 0
                return False
    return True

calls_mrv = 0
def solve_mrv(board):
    global calls_mrv
    calls_mrv += 1
    min_options = 10
    best_r, best_c = -1, -1
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = sum(1 for v in range(1, 10) if is_valid(board, r, c, v))
                if options < min_options:
                    min_options = options
                    best_r, best_c = r, c
                if min_options == 0: return False 
                if min_options == 1: break 
    if best_r == -1: return True 
    for val in range(1, 10):
        if is_valid(board, best_r, best_c, val):
            board[best_r][best_c] = val
            if solve_mrv(board): return True
            board[best_r][best_c] = 0
    return False
grid_seq = copy.deepcopy(original_grid)
t0 = time.time()
solve_seq(grid_seq)
t1 = time.time()
print(f"Quet Tuan Tu: Loi goi = {calls_seq}, Thoi gian = {(t1-t0)*1000:.2f} ms")

grid_mrv = copy.deepcopy(original_grid)
t0 = time.time()
solve_mrv(grid_mrv)
t1 = time.time()
print(f"Heuristic MRV: Loi goi = {calls_mrv}, Thoi gian = {(t1-t0)*1000:.2f} ms")

print(f"Loi giai giong nhau? {grid_seq == grid_mrv}")