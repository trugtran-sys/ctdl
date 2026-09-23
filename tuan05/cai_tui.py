weights = [2, 3, 4, 5, 7]
values = [3, 7, 9, 12, 16]
names = ["A", "B", "C", "D", "E"]
W = 11
n = len(weights)
f = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(W + 1):
        f[i][j] = f[i - 1][j]
        if weights[i - 1] <= j:
            f[i][j] = max(
                f[i][j],
                f[i - 1][j - weights[i - 1]] + values[i - 1]
            )
chosen = []
j = W
for i in range(n, 0, -1):
    if f[i][j] != f[i - 1][j]:
        chosen.append(i - 1)
        j -= weights[i - 1]
chosen.reverse()
print("Bang f:")
print("     ", *range(W + 1))
for i in range(n + 1):
    print(f"{i:2} : ", *f[i])
print("Gia tri lon nhat:", f[n][W])
print("Do vat duoc chon:", [names[i] for i in chosen])
print("Tong trong luong:", sum(weights[i] for i in chosen))
print("So o cua bang:", (n + 1) * (W + 1))