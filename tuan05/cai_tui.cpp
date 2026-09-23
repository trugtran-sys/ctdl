#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> weights = {2, 3, 4, 5, 7};
    vector<int> values = {3, 7, 9, 12, 16};
    vector<char> names = {'A', 'B', 'C', 'D', 'E'};
    const int W = 11;
    const int n = weights.size();
    vector<vector<int>> f(n + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= W; ++j) {
            f[i][j] = f[i - 1][j];
            if (weights[i - 1] <= j) {
                f[i][j] = max(
                    f[i][j],
                    f[i - 1][j - weights[i - 1]] + values[i - 1]
                );
            }
        }
    }
    vector<int> chosen;
    int j = W;
    for (int i = n; i >= 1; --i) {
        if (f[i][j] != f[i - 1][j]) {
            chosen.push_back(i - 1);
            j -= weights[i - 1];
        }
    }
    reverse(chosen.begin(), chosen.end());
    cout << "Bang f:\n";
    cout << "     ";
    for (int j = 0; j <= W; ++j)
        cout << j << ' ';
    cout << '\n';
    for (int i = 0; i <= n; ++i) {
        cout << i << " :  ";
        for (int j = 0; j <= W; ++j)
            cout << f[i][j] << ' ';
        cout << '\n';
    }
    cout << "Gia tri lon nhat: " << f[n][W] << '\n';
    cout << "Do vat duoc chon: ";
    for (int index : chosen)
        cout << names[index] << ' ';
    cout << '\n';
    int totalWeight = 0;
    for (int index : chosen)
        totalWeight += weights[index];
    cout << "Tong trong luong: " << totalWeight << '\n';
    cout << "So o cua bang: " << (n + 1) * (W + 1) << '\n';
    return 0;
}