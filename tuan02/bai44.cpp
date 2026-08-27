#include <iostream>
#include <chrono>
#include <vector>
#include <iomanip>

using namespace std;
volatile long long dummy = 0;
void thuat_toan_o_n2(int n) {
    long long tong = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tong += (i + j);
        }
    }
    dummy = tong;
}
int main() {
    vector<int> sizes = {500, 1000, 2000, 4000};
    vector<double> times;
    cout << fixed << setprecision(5);
    for (size_t k = 0; k < sizes.size(); k++) {
        int n = sizes[k];
        double min_time = 1e9;
        for (int run = 0; run < 3; run++) {
            auto t0 = chrono::steady_clock::now();
            thuat_toan_o_n2(n);
            auto t1 = chrono::steady_clock::now();
            double giay = chrono::duration<double>(t1 - t0).count();
            if (giay < min_time) min_time = giay;
        }
        times.push_back(min_time);
        if (k == 0) {
            cout << "n = " << n << " -> Thoi gian min: " << min_time << " s\n";
        } else {
            double ratio = min_time / times[k - 1];
            cout << "n = " << n << " -> Thoi gian min: " << min_time << " s | Ti le: " << ratio << "\n";
        }
    }
    return 0;
}