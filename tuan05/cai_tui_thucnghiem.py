import random
import time
weights = [2, 3, 4, 5, 7]
values = [3, 7, 9, 12, 16]
W = 11
def two_dimension(w, v, capacity):
    n = len(w)
    f = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            f[i][j] = f[i - 1][j]
            if w[i - 1] <= j:
                f[i][j] = max(
                    f[i][j],
                    f[i - 1][j - w[i - 1]] + v[i - 1]
                )

    return f
def one_dimension_decreasing(w, v, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(w, v):
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp
def one_dimension_increasing(w, v, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(w, v):
        for j in range(weight, capacity + 1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp
def print_main_result():
    f = two_dimension(weights, values, W)
    chosen = []
    capacity = W

    for i in range(len(weights), 0, -1):
        if f[i][capacity] != f[i - 1][capacity]:
            chosen.append(i - 1)
            capacity -= weights[i - 1]

    chosen.reverse()

    print("Bang f:")
    print("     " + " ".join(f"{j:2}" for j in range(W + 1)))

    for i, row in enumerate(f):
        print(f"{i:2}:  " + " ".join(f"{x:2}" for x in row))

    print("Gia tri lon nhat:", f[-1][W])
    print("Do vat duoc chon:", " ".join("ABCDE"[i] for i in chosen))
    print("Tong trong luong:", sum(weights[i] for i in chosen))
    print("So o cua bang:", (len(weights) + 1) * (W + 1))
def print_table_22():
    two = two_dimension(weights, values, W)[-1][W]
    decrease = one_dimension_decreasing(weights, values, W)[W]
    increase = one_dimension_increasing(weights, values, W)[W]

    print("Phuong phap                         f[W]  So o  Dung 0/1")
    print(f"Ban hai chieu                      {two:4}    72       Co")
    print(f"Ban mot chieu, j giam              {decrease:4}    12       Co")
    print(f"Ban mot chieu, j tang              {increase:4}    12     Khong")
def benchmark():
    random.seed(2026)
    w = [random.randint(1, 100) for _ in range(100)]
    v = [random.randint(1, 100) for _ in range(100)]
    print("W        So o cua bang f       Thoi gian (ms)   Gap lan")
    previous = None
    for capacity in [10**3, 10**4, 10**5, 10**6]:
        start = time.perf_counter()
        result = one_dimension_decreasing(w, v, capacity)
        elapsed = (time.perf_counter() - start) * 1000
        cells = (len(w) + 1) * (capacity + 1)
        ratio = "-" if previous is None else f"{elapsed / previous:.2f}"
        print(f"{capacity:<8} {cells:<22} {elapsed:<16.3f} {ratio}")
        assert result[capacity] >= 0
        previous = elapsed
if __name__ == "__main__":
    print_main_result()
    print_table_22()
    benchmark()