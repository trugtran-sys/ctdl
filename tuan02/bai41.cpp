#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
long long tich_lon_nhat(const vector<int>& a) {
    if (a.empty()) return 0;
    long long best = a[0];
    long long max_end = a[0];
    long long min_end = a[0];
    for (int i = 1; i < (int)a.size(); i++) {
        long long val = a[i];
        if (val < 0) {
            swap(max_end, min_end); 
        }
        max_end = max(val, max_end * val);
        min_end = min(val, min_end * val);
        best = max(best, max_end);
    }
    return best;
}
long long tich_lon_nhat_n2(const vector<int>& a) {
    if (a.empty()) return 0;
    long long best = a[0];
    
    for (int i = 0; i < (int)a.size(); i++) {
        long long cur = 1;
        for (int j = i; j < (int)a.size(); j++) {
            cur *= a[j];
            best = max(best, cur);
        }
    }
    return best;
}
int main() {
    int n;
    while (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        cout << tich_lon_nhat(a) << "\n";
    }
    return 0;
}