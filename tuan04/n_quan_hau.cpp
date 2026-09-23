#include <iostream>
#include <vector>

using namespace std;
int n;
long long so_nut = 0;
int so_loi_giai = 0;
vector<int> first_sol;
vector<bool> cot, cheo1, cheo2;
vector<int> x;
void backtrack(int i) {
    so_nut++;
    if (i > n) {
        so_loi_giai++;
        if (first_sol.empty()) {
            first_sol.assign(x.begin() + 1, x.begin() + n + 1);
        }
        return;
    }
    for (int j = 1; j <= n; ++j) {
        if (cot[j] && cheo1[i - j + n] && cheo2[i + j - 1]) {
            x[i] = j;
            cot[j] = cheo1[i - j + n] = cheo2[i + j - 1] = false;
            backtrack(i + 1);
            cot[j] = cheo1[i - j + n] = cheo2[i + j - 1] = true;
        }
    }
}
int main() {
    cout << "Nhap n: ";
    cin >> n;
    cot.assign(n + 1, true);
    cheo1.assign(2 * n + 1, true);
    cheo2.assign(2 * n + 1, true);
    x.resize(n + 1);
    backtrack(1);
    cout << "So nut da duyet: " << so_nut << endl;
    cout << "So loi giai: " << so_loi_giai << endl;
    if (!first_sol.empty()) {
        cout << "Ban co loi giai dau tien (x): ";
        for (int val : first_sol) cout << val << " ";
        cout << endl;
    }
    return 0;
}