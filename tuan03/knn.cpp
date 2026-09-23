#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

struct Neighbor {
    double dist;
    int label;
};
int knn_predict(const std::vector<std::vector<double>>& X_train, const std::vector<int>& y_train, const std::vector<double>& x_test, int k) {
    std::vector<Neighbor> distances;
    for (size_t i = 0; i < X_train.size(); i++) {
        double sum = 0;
        for (size_t j = 0; j < x_test.size(); j++) {
            sum += pow(X_train[i][j] - x_test[j], 2);
        }
        distances.push_back({sqrt(sum), y_train[i]});
    }
    std::sort(distances.begin(), distances.end(), [](const Neighbor& a, const Neighbor& b) {
        return a.dist < b.dist;
    });
    int count0 = 0, count1 = 0;
    for (int i = 0; i < k; i++) {
        if (distances[i].label == 0) count0++;
        else count1++;
    }
    return (count0 > count1) ? 0 : 1;
}
int main() {
    std::vector<std::vector<double>> X_train = {{1, 2}, {2, 3}, {3, 1}, {6, 5}, {7, 7}, {8, 6}};
    std::vector<int> y_train = {0, 0, 0, 1, 1, 1};
    std::vector<double> x_test = {2, 2};
    std::cout << "C++ KNN Result: " << knn_predict(X_train, y_train, x_test, 3) << std::endl;
    return 0;
}