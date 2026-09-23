#include <bits/stdc++.h>
using namespace std;
pair<int, vector<int>> greedy(vector<int> coins, int S) {
    sort(coins.rbegin(), coins.rend());
    int remaining = S;
    vector<int> result;
    for (int coin : coins)
        while (remaining >= coin) { remaining -= coin; result.push_back(coin); }
    return {(int)result.size(), result};
}
pair<int, vector<int>> dp_coin(vector<int>& coins, int S) {
    const int INF = 1e9;
    vector<int> f(S + 1, INF), last(S + 1, -1);
    f[0] = 0;
    for (int i = 1; i <= S; i++)
        for (int c : coins)
            if (c <= i && f[i - c] + 1 < f[i]) { f[i] = f[i - c] + 1; last[i] = c; }
    vector<int> result;
    for (int cur = S; cur > 0; cur -= last[cur]) result.push_back(last[cur]);
    return {f[S], result};
}
int main() {
    vector<pair<vector<int>, int>> sets = {
        {{1, 4, 6, 9},       12},
        {{1, 5, 10, 20, 50}, 85},
        {{1, 3, 7, 12},      20},
        {{1, 2, 5, 10},      38},
        {{1, 6, 10},         12},
        {{1, 4, 5, 15, 20},  23},
    };
    for (int i = 0; i < 6; i++) {
        auto& [coins, S] = sets[i];
        auto [g_n, g_r] = greedy(coins, S);
        auto [d_n, d_r] = dp_coin(coins, S);
        string correct = (g_n == d_n) ? "Dung" : "SAI";
        sort(g_r.rbegin(), g_r.rend());
        sort(d_r.rbegin(), d_r.rend());
        auto v2s = [](vector<int>& v) {
            string s = "[";
            for (int j = 0; j < (int)v.size(); j++) s += (j ? "," : "") + to_string(v[j]);
            return s + "]";
        };
        cout << "Bo " << i+1 << ": TL=" << g_n << "to " << v2s(g_r)
             << " | TU=" << d_n << "to " << v2s(d_r)
             << " | " << correct << "\n";
    }
    return 0;
}