#include <iostream>
#include <vector>

using namespace std;
struct KetQua { 
    long long tong; 
    int dau, cuoi; 
};
KetQua kadane_chi_so(const vector<long long>& a) {
    long long best = a[0], cur = a[0];
    int l = 0, r = 0, bat_dau = 0;
    for (int i = 1; i < (int)a.size(); i++) {
        if (cur + a[i] >= a[i]) {
            cur += a[i];
        } else {
            cur = a[i];
            bat_dau = i;
        }
        if (cur > best) {
            best = cur;
            l = bat_dau;
            r = i;
        }
    }
    return {best, l + 1, r + 1};
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    while (cin >> n) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        KetQua kq = kadane_chi_so(a);
        printf("tong %lld, doan [%d..%d]\n", kq.tong, kq.dau, kq.cuoi);
    }
    return 0;
}