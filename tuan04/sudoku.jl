original_grid = [
    0 0 0 0 0 6 0 0 0;
    0 8 1 0 5 0 4 0 0;
    0 0 9 0 0 7 0 5 8;
    0 0 0 9 0 0 0 0 0;
    0 0 6 0 0 1 0 0 7;
    7 4 0 0 0 0 2 0 1;
    0 0 0 1 3 0 0 0 4;
    0 0 0 0 2 9 0 0 0;
    9 0 0 0 0 8 0 6 0
]
function is_valid(board, r, c, val)
    for i in 1:9
        if board[r, i] == val || board[i, c] == val
            return false
        end
        br, bc = 3 * div(r - 1, 3) + div(i - 1, 3) + 1, 3 * div(c - 1, 3) + (i - 1) % 3 + 1
        if board[br, bc] == val
            return false
        end
    end
    return true
end
global calls_seq = 0
function solve_seq(board)
    global calls_seq
    calls_seq += 1
    for r in 1:9
        for c in 1:9
            if board[r, c] == 0
                for val in 1:9
                    if is_valid(board, r, c, val)
                        board[r, c] = val
                        if solve_seq(board) return true end
                        board[r, c] = 0
                    end
                end
                return false
            end
        end
    end
    return true
end
global calls_mrv = 0
function solve_mrv(board)
    global calls_mrv
    calls_mrv += 1
    min_options = 10
    best_r, best_c = -1, -1
    for r in 1:9
        for c in 1:9
            if board[r, c] == 0
                options = 0
                for val in 1:9
                    if is_valid(board, r, c, val); options += 1; end
                end
                if options < min_options
                    min_options = options
                    best_r, best_c = r, c
                end
                if min_options == 0 return false end
                if min_options == 1 @goto found end
            end
        end
    end
    @label found
    if best_r == -1 return true end
    for val in 1:9
        if is_valid(board, best_r, best_c, val)
            board[best_r, best_c] = val
            if solve_mrv(board) return true end
            board[best_r, best_c] = 0
        end
    end
    return false
end
grid_seq = copy(original_grid)
time_seq = @elapsed solve_seq(grid_seq)
println("Quet Tuan Tu: Loi goi = $calls_seq, Thoi gian = $(time_seq * 1000) ms")
grid_mrv = copy(original_grid)
time_mrv = @elapsed solve_mrv(grid_mrv)
println("Heuristic MRV: Loi goi = $calls_mrv, Thoi gian = $(time_mrv * 1000) ms")
println("Loi giai giong nhau? ", grid_seq == grid_mrv)