#include <iostream>
#include <vector>

void insertion_sort_cpp(std::vector<int>& arr) {
    for (int i = 1; i < (int)arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
int main() {
    std::vector<int> A = {8, 3, 5, 1, 9, 2};
    insertion_sort_cpp(A);
    std::cout << "C++: ";
    for (int num : A) std::cout << num << " ";
    return 0;
}