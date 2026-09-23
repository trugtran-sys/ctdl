#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
int original_grid[9][9] = {
    {0, 0, 0, 0, 0, 6, 0, 0, 0},
    {0, 8, 1, 0, 5, 0, 4, 0, 0},
    {0, 0, 9, 0, 0, 7, 0, 5, 8},
    {0, 0, 0, 9, 0, 0, 0, 0, 0},
    {0, 0, 6, 0, 0, 1, 0, 0, 7},
    {7, 4, 0, 0, 0, 0, 2, 0, 1},
    {0, 0, 0, 1, 3, 0, 0, 0, 4},
    {0, 0, 0, 0, 2, 9, 0, 0, 0},
    {9, 0, 0, 0, 0, 8, 0, 6, 0}
};
bool isValid(int board[9][9], int r, int c, int val) {
    for (int i = 0; i < 9; i++) {
        if (board[r][i] == val || board[i][c] == val) return false;
        if (board[3 * (r / 3) + i / 3][3 * (c / 3) + i % 3] == val) return false;
    }
    return true;
}
long long calls_seq = 0;
bool solve_seq(int board[9][9]) {
    calls_seq++;
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (board[r][c] == 0) {
                for (int val = 1; val <= 9; val++) {
                    if (isValid(board, r, c, val)) {
                        board[r][c] = val;
                        if (solve_seq(board)) return true;
                        board[r][c] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}
long long calls_mrv = 0;
bool solve_mrv(int board[9][9]) {
    calls_mrv++;
    int min_options = 10;
    int best_r = -1, best_c = -1;

    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (board[r][c] == 0) {
                int options = 0;
                for (int val = 1; val <= 9; val++) {
                    if (isValid(board, r, c, val)) options++;
                }
                if (options < min_options) {
                    min_options = options;
                    best_r = r; best_c = c;
                }
                if (min_options == 0) return false; 
                if (min_options == 1) goto found; 
            }
        }
    }
    found:
    if (best_r == -1) return true; 

    for (int val = 1; val <= 9; val++) {
        if (isValid(board, best_r, best_c, val)) {
            board[best_r][best_c] = val;
            if (solve_mrv(board)) return true;
            board[best_r][best_c] = 0;
        }
    }
    return false;
}
void copyGrid(int src[9][9], int dest[9][9]) {
    for(int i=0; i<9; i++) for(int j=0; j<9; j++) dest[i][j] = src[i][j];
}
bool compareGrid(int a[9][9], int b[9][9]) {
    for(int i=0; i<9; i++) for(int j=0; j<9; j++) if(a[i][j] != b[i][j]) return false;
    return true;
}
int main() {
    int grid_seq[9][9], grid_mrv[9][9];
    copyGrid(original_grid, grid_seq);
    auto start_seq = chrono::high_resolution_clock::now();
    solve_seq(grid_seq);
    auto end_seq = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> time_seq = end_seq - start_seq;
    cout << "Quet Tuan Tu: Loi goi = " << calls_seq << ", Thoi gian = " << time_seq.count() << " ms\n";

    copyGrid(original_grid, grid_mrv);
    auto start_mrv = chrono::high_resolution_clock::now();
    solve_mrv(grid_mrv);
    auto end_mrv = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> time_mrv = end_mrv - start_mrv;
    cout << "Heuristic MRV: Loi goi = " << calls_mrv << ", Thoi gian = " << time_mrv.count() << " ms\n";
    cout << "Loi giai giong nhau? " << (compareGrid(grid_seq, grid_mrv) ? "True" : "False") << "\n";
    return 0;
}