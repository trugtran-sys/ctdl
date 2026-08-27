#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;
bool la_nguyen_to(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}
vector<int> sang_eratosthenes(int n) {
    if (n < 2) return {};
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; (long long)p * p <= n; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= n; i += p)
                is_prime[i] = false;
        }
    }
    vector<int> primes;
    for (int p = 2; p <= n; ++p) {
        if (is_prime[p]) primes.push_back(p);
    }
    return primes;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        auto t1_start = high_resolution_clock::now();
        long long sum_dummy = 0;
        for (int i = 2; i <= n; ++i) {
            if (la_nguyen_to(i)) sum_dummy += i;
        }
        auto t1_end = high_resolution_clock::now();
        double t_tung_so = duration<double>(t1_end - t1_start).count();
        auto t2_start = high_resolution_clock::now();
        vector<int> primes = sang_eratosthenes(n);
        auto t2_end = high_resolution_clock::now();
        double t_sang = duration<double>(t2_end - t2_start).count();
        if (sum_dummy == -1) cout << sum_dummy;
        if (n == 30) {
            for (int p : primes) cout << p << " ";
            cout << "(" << primes.size() << " so)\n";
        } else if (n == 1000000) {
            long long sum = 0;
            for (int p : primes) sum += p;
            cout << "so luong = " << primes.size() << ", tong = " << sum << "\n";
        } else {
            cout << "so luong = " << primes.size() << "\n";
        }
        cout << "Thoi gian: Tung so = " << t_tung_so << "s | Sang = " << t_sang << "s\n";
    }
    return 0;
}