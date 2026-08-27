#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;
long long cach1(const vector<int>& a) {
    int n = a.size();
    long long max_sum = LLONG_MIN;
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            long long sum = 0;
            for (int k = i; k <= j; ++k) sum += a[k];
            max_sum = max(max_sum, sum);
        }
    }
    return max_sum;
}
long long cach2(const vector<int>& a) {
    int n = a.size();
    long long max_sum = LLONG_MIN;
    for (int i = 0; i < n; ++i) {
        long long sum = 0;
        for (int j = i; j < n; ++j) {
            sum += a[j];
            max_sum = max(max_sum, sum);
        }
    }
    return max_sum;
}
long long kadane(const vector<int>& a) {
    long long max_so_far = a[0], curr_max = a[0];
    for (size_t i = 1; i < a.size(); ++i) {
        curr_max = max((long long)a[i], curr_max + a[i]);
        max_so_far = max(max_so_far, curr_max);
    }
    return max_so_far;
}
void do_thoi_gian() {
    vector<int> sizes = {200, 400, 800};
    mt19937 rng(42);
    uniform_int_distribution<int> dist(-100, 100);
    volatile long long dummy = 0;
    cout << fixed << setprecision(6);
    for (int c = 1; c <= 3; ++c) {
        vector<double> times;
        for (int n : sizes) {
            vector<int> a(n);
            for (int &x : a) x = dist(rng);
            int runs = (c == 1) ? 5 : (c == 2) ? 1000 : 200000;
            auto start = chrono::high_resolution_clock::now();
            for (int r = 0; r < runs; ++r) {
                if (c == 1) dummy += cach1(a);
                else if (c == 2) dummy += cach2(a);
                else dummy += kadane(a);
            }
            auto end = chrono::high_resolution_clock::now();
            chrono::duration<double> diff = end - start;
            times.push_back(diff.count() / runs);
        }
        cout << times[0] << " " << times[1] << " " << times[2] << "\n";
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    while (cin >> n) {
        if (n == 0) {
            do_thoi_gian();
        } else {
            vector<int> a(n);
            for (int i = 0; i < n; ++i) cin >> a[i];
            cout << kadane(a) << "\n";
        }
    }
    return 0;
}