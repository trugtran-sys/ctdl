def greedy(coins, S):
    sorted_coins = sorted(coins, reverse=True)
    remaining = S
    result = []
    for coin in sorted_coins:
        while remaining >= coin:
            remaining -= coin
            result.append(coin)
    return len(result), result
def dp_coin(coins, S):
    INF = float('inf')
    f = [INF] * (S + 1)
    last = [-1] * (S + 1)
    f[0] = 0
    for i in range(1, S + 1):
        for c in coins:
            if c <= i and f[i - c] + 1 < f[i]:
                f[i] = f[i - c] + 1
                last[i] = c
    result = []
    cur = S
    while cur > 0:
        result.append(last[cur])
        cur -= last[cur]
    return f[S], result
sets = [
    ([1, 4, 6, 9],       12),
    ([1, 5, 10, 20, 50], 85),
    ([1, 3, 7, 12],      20),
    ([1, 2, 5, 10],      38),
    ([1, 6, 10],         12),
    ([1, 4, 5, 15, 20],  23),
]
for i, (coins, S) in enumerate(sets, 1):
    g_n, g_r = greedy(coins, S)
    d_n, d_r = dp_coin(coins, S)
    correct = "Dung" if g_n == d_n else "SAI"
    print(f"Bo {i}: TL={g_n}to {sorted(g_r,reverse=True)} | TU={d_n}to {sorted(d_r,reverse=True)} | {correct}")