function greedy(coins, S)
    sorted_coins = sort(coins, rev=true)
    remaining = S
    result = Int[]
    for coin in sorted_coins
        while remaining >= coin
            remaining -= coin
            push!(result, coin)
        end
    end
    return length(result), result
end
function dp_coin(coins, S)
    INF = typemax(Int) ÷ 2
    f    = fill(INF, S + 1)   # f[i+1] ↔ dp[i]
    last = zeros(Int, S + 1)
    f[1] = 0
    for i in 1:S
        for c in coins
            if c <= i && f[i - c + 1] + 1 < f[i + 1]
                f[i + 1] = f[i - c + 1] + 1
                last[i + 1] = c
            end
        end
    end
    result = Int[]
    cur = S
    while cur > 0
        push!(result, last[cur + 1])
        cur -= last[cur + 1]
    end
    return f[S + 1], result
end
sets = [
    ([1, 4, 6, 9],       12),
    ([1, 5, 10, 20, 50], 85),
    ([1, 3, 7, 12],      20),
    ([1, 2, 5, 10],      38),
    ([1, 6, 10],         12),
    ([1, 4, 5, 15, 20],  23),
]
for (i, (coins, S)) in enumerate(sets)
    g_n, g_r = greedy(coins, S)
    d_n, d_r = dp_coin(coins, S)
    correct = g_n == d_n ? "Dung" : "SAI"
    println("Bo $i: TL=$(g_n)to $(sort(g_r,rev=true)) | TU=$(d_n)to $(sort(d_r,rev=true)) | $correct")
end