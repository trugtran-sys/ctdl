function knn_predict(X_train, y_train, x_test, k)
    distances = []
    for i in 1:length(X_train)
        dist = sqrt(sum((X_train[i] .- x_test).^2))
        push!(distances, (dist, y_train[i]))
    end
    sort!(distances, by = x -> x[1])
    neighbors = [distances[i][2] for i in 1:k]
    return argmax(counter(neighbors))
end
X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]]
y_train = [0, 0, 0, 1, 1, 1]
x_test = [2, 2]
println("Julia code setup ready.")