#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;
int matrix[5][5] = {
    {0, 10, 9, 22, 23},
    {10, 0, 16, 19, 14},
    {9, 16, 0, 7, 28},
    {22, 19, 7, 0, 8},
    {23, 14, 28, 8, 0}
};
int n = 5, c_min = 7;
int nodes, best_cost;
vector<int> best_path;
bool visited[5];
void solve(int step, int u, int cur_cost, bool use_bound, vector<int>& path) {
    nodes++;
    if (use_bound && cur_cost + (n - step + 1) * c_min >= best_cost) {
        return;
    }
    if (step == n) {
        if (cur_cost + matrix[u][0] < best_cost) {
            best_cost = cur_cost + matrix[u][0];
            best_path = path;
            best_path.push_back(0);
        }
        return;
    }
    for (int v = 1; v < n; v++) {
        if (!visited[v]) {
            visited[v] = true;
            path.push_back(v);
            solve(step + 1, v, cur_cost + matrix[u][v], use_bound, path);
            path.pop_back();
            visited[v] = false;
        }
    }
}
int main() {
    vector<int> path;
    nodes = 0; best_cost = INF; path.clear();
    for(int i=0; i<n; i++) visited[i] = false;
    visited[0] = true; path.push_back(0);
    solve(1, 0, 0, false, path);
    cout << "KHONG cat nhanh: Cost = " << best_cost << ", Nodes = " << nodes << "\n";
    nodes = 0; best_cost = INF; path.clear();
    for(int i=0; i<n; i++) visited[i] = false;
    visited[0] = true; path.push_back(0);
    solve(1, 0, 0, true, path);
    cout << "CO cat nhanh: Cost = " << best_cost << ", Nodes = " << nodes << "\n";
    return 0;
}