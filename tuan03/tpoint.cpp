#include <iostream>
#include <vector>
#include <algorithm>

void find_pair_with_sum(std::vector<int>& arr, int S) {
    std::sort(arr.begin(), arr.end()); 
    int left = 0;
    int right = (int)arr.size() - 1;
    while (left < right) {
        int current_sum = arr[left] + arr[right];
        if (current_sum == S) {
            std::cout << "C++ Pair found: " << arr[left] << " and " << arr[right] << std::endl;
            return;
        } else if (current_sum < S) {
            left++;
        } else {
            right--;
        }
    }
    std::cout << "C++ No pair found." << std::endl;
}
int main() {
    std::vector<int> A = {8, 3, 5, 1, 9, 2};
    int S = 10;
    find_pair_with_sum(A, S);
    return 0;
}