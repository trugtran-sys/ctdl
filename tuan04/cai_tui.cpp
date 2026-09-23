#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    string name; int v, w; double vw;
};
bool compareItem(Item a, Item b) { return a.vw > b.vw; }
int n, W = 14, best_v = 0, nodes = 0;
vector<string> best_subset;
vector<Item> items = {
    {"A", 19, 4}, {"B", 25, 7}, {"C", 7, 3}, 
    {"D", 8, 3}, {"E", 9, 3}, {"F", 21, 10}
};
double bound(int i, int cur_w, int cur_v) {
    if (cur_w >= W) return 0;
    double profit = cur_v; int totw = cur_w, j = i;
    while (j < n && totw + items[j].w <= W) {
        totw += items[j].w;
        profit += items[j].v;
        j++;
    }
    if (j < n) profit += (W - totw) * items[j].vw;
    return profit;
}
void solve(int i, int cur_w, int cur_v, bool use_bound, vector<string>& cur_subset) {
    nodes++;
    if (cur_v > best_v) {
        best_v = cur_v; best_subset = cur_subset;
    }
    if (i == n) return;
    if (use_bound && bound(i, cur_w, cur_v) <= best_v) return;
    
    if (cur_w + items[i].w <= W) {
        cur_subset.push_back(items[i].name);
        solve(i + 1, cur_w + items[i].w, cur_v + items[i].v, use_bound, cur_subset);
        cur_subset.pop_back();
    }
    solve(i + 1, cur_w, cur_v, use_bound, cur_subset);
}
int main() {
    for (auto& item : items) item.vw = (double)item.v / item.w;
    sort(items.begin(), items.end(), compareItem);
    n = items.size();
    vector<string> cur_subset;
    solve(0, 0, 0, false, cur_subset);
    cout << "KHONG cat nhanh: Max Value = " << best_v << ", Nodes = " << nodes << endl;
    nodes = 0; best_v = 0; best_subset.clear();
    solve(0, 0, 0, true, cur_subset);
    cout << "CO cat nhanh: Max Value = " << best_v << ", Nodes = " << nodes << endl;
    return 0;
}