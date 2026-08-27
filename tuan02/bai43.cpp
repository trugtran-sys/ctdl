#include <iostream>
#include <vector>
#include <climits>
#include <iomanip>

using namespace std;
long long dem_goi = 0;
const int GIOI_HAN_DE_QUY = 35; 
long long fib_de_quy(int n) {
    dem_goi++;
    if (n <= 2) return 1;
    return fib_de_quy(n - 1) + fib_de_quy(n - 2);
}
long long fib_ghi_nho(int n, vector<long long>& mem) {
    if (n <= 2) return 1;
    if (mem[n] != -1) return mem[n];
    mem[n] = fib_ghi_nho(n - 1, mem) + fib_ghi_nho(n - 2, mem);
    return mem[n];
}
bool fib_lap(int n, long long& ket_qua) {
    if (n <= 2) {
        ket_qua = 1;
        return true;
    }
    long long f1 = 1, f2 = 1, fn;
    for (int i = 3; i <= n; i++) {
        if (LLONG_MAX - f1 < f2) return false;
        fn = f1 + f2;
        f1 = f2;
        f2 = fn;
    }
    ket_qua = f2;
    return true;
}
int main() {
    int n;
    if (!(cin >> n)) return 0;
    cout << "n = " << n << "\n";
    long long kq_lap;
    if (!fib_lap(n, kq_lap)) {
        cout << "Loi: F_" << n << " vuot qua kieu long long (F_92 la max)\n";
        return 0;
    }
    if (n <= GIOI_HAN_DE_QUY) {
        dem_goi = 0;
        long long kq_dq = fib_de_quy(n);
        cout << "De quy thuan: F = " << kq_dq << ", so loi goi = " << dem_goi << "\n";
    } else {
        double uoc_luong_goi = 2.0 * kq_lap - 1;
        cout << "De quy thuan: Bo qua (uoc tinh co " << scientific << setprecision(2) 
             << uoc_luong_goi << " loi goi, qua lau)\n";
    }
    vector<long long> bang_nho(n + 1, -1);
    cout << "Ghi nho     : F = " << fib_ghi_nho(n, bang_nho) << "\n";
    cout << "Vong lap    : F = " << kq_lap << "\n";
    return 0;
}