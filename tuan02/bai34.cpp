#include <iostream>
#include <cmath>

using namespace std;
long long dao_nguoc(long long n) {
    long long res = 0;
    long long temp = abs(n);
    while (temp > 0) {
        res = res * 10 + temp % 10;
        temp /= 10;
    }
    return n < 0 ? -res : res;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    if (cin >> n) {
        cout << dao_nguoc(n) << "\n";
    }
    return 0;
}