function cai_tui()
    weights = [2, 3, 4, 5, 7]
    values = [3, 7, 9, 12, 16]
    names = ["A", "B", "C", "D", "E"]
    W = 11
    n = length(weights)
    f = zeros(Int, n + 1, W + 1)
    for i in 1:n
        for capacity in 0:W
            f[i + 1, capacity + 1] = f[i, capacity + 1]

            if weights[i] <= capacity
                f[i + 1, capacity + 1] = max(
                    f[i + 1, capacity + 1],
                    f[i, capacity - weights[i] + 1] + values[i]
                )
            end
        end
    end
    chosen = Int[]
    capacity = W
    for i in n:-1:1
        if f[i + 1, capacity + 1] != f[i, capacity + 1]
            pushfirst!(chosen, i)
            capacity -= weights[i]
        end
    end
    println("Bang f:")
    println("     ", join(0:W, " "))
    for i in 1:(n + 1)
        println(i - 1, " :  ", join(f[i, :], " "))
    end
    println("Gia tri lon nhat: ", f[n + 1, W + 1])
    println("Do vat duoc chon: ", names[chosen])
    println("Tong trong luong: ", sum(weights[chosen]))
    println("So o cua bang: ", (n + 1) * (W + 1))
end
cai_tui()