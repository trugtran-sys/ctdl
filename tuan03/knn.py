import math

def knn_predict(X_train, y_train, x_test, k):
    distances = []
    for i in range(len(X_train)):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(X_train[i], x_test)))
        distances.append((dist, y_train[i]))
    distances.sort(key=lambda x: x[0])
    neighbors = [distances[i][1] for i in range(k)]
    return max(set(neighbors), key=neighbors.count)
X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]]
y_train = [0, 0, 0, 1, 1, 1]
x_test = [2, 2]
print("Python KNN Result:", knn_predict(X_train, y_train, x_test, 3))