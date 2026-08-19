#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    long long sum = 0;
    long long max_val = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        sum += x;
        if (i == 0 || x > max_val) {
            max_val = x;
        }
    }
    cout << sum << " " << max_val << "\n";
    return 0;
}