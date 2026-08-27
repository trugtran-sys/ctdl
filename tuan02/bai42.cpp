#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <iomanip>

using namespace std;
volatile long long dummy_result = 0;
pair<long long, int> cua_so_truot(const vector<int>& a, int k) {
    long long current_sum = 0;
    for (int i = 0; i < k; i++) current_sum += a[i];
    long long max_sum = current_sum;
    int start_index = 0;
    for (int i = k; i < (int)a.size(); i++) {
        current_sum += a[i] - a[i - k];
        if (current_sum > max_sum) {
            max_sum = current_sum;
            start_index = i - k + 1;
        }
    }
    return {max_sum, start_index + 1};
}
void cua_so_truot_ngay_tho(const vector<int>& a, int k) {
    long long max_sum = -1e18;
    for (int i = 0; i <= (int)a.size() - k; i++) {
        long long current_sum = 0;
        for (int j = i; j < i + k; j++) current_sum += a[j];
        if (current_sum > max_sum) max_sum = current_sum;
    }
    dummy_result = max_sum; 
}
void do_thoi_gian() {
    int n = 1000000, k = 1000;
    vector<int> a(n);
    for (int i = 0; i < n; i++) a[i] = rand() % 200 - 100;
    auto t1 = chrono::high_resolution_clock::now();
    cua_so_truot_ngay_tho(a, k);
    auto t2 = chrono::high_resolution_clock::now();
    double t_naive = chrono::duration<double>(t2 - t1).count();
    auto t3 = chrono::high_resolution_clock::now();
    pair<long long, int> res = cua_so_truot(a, k);
    dummy_result = res.first;
    auto t4 = chrono::high_resolution_clock::now();
    double t_window = chrono::duration<double>(t4 - t3).count();
    cout << fixed << setprecision(4);
    cout << "[Do thoi gian n=10^6, k=1000] C++ | O(n*k): " << t_naive << "s | O(n): " << t_window << "s | Nhanh hon: " << (t_naive / t_window) << "x\n";
}
int main() {
    int n, k;
    if (cin >> n >> k) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        pair<long long, int> kq = cua_so_truot(a, k);
        cout << "tong " << kq.first << ", bat dau tai vi tri " << kq.second << "\n";
        do_thoi_gian();
    }
    return 0;
}