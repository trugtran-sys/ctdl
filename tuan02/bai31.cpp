#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n) || n <= 0) return 0;
    long long x;
    cin >> x;
    long long tong = x;
    long long nho_nhat = x;
    long long lon_nhat = x;
    for (int i = 1; i < n; ++i) {
        cin >> x;
        tong += x;
        if (x < nho_nhat) nho_nhat = x;
        if (x > lon_nhat) lon_nhat = x;
    }
    double trung_binh = (double)tong / n;
    cout << tong << " " << fixed << setprecision(4) << trung_binh << " " 
         << nho_nhat << " " << lon_nhat << "\n";  
    return 0;
}