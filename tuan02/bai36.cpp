#include <iostream>
#include <climits>

using namespace std;
bool giai_thua(int n, long long &kq) {
    if (n < 0) return false;
    kq = 1;
    for (int i = 1; i <= n; ++i) {
        if (kq > LLONG_MAX / i) {
            return false;
        }
        kq *= i;
    }
    return true;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        long long kq;
        if (giai_thua(n, kq)) {
            cout << kq << "\n";
        } else {
            cout << "TRAN SO (21! = 5109094217170944000 > 9223372036854775807)\n";
        }
    }
    return 0;
}