from time import perf_counter

def thuat_toan_o_n2(n):
    tong = 0
    for i in range(n):
        for j in range(n):
            tong += i + j
    return tong
def do_thoi_gian(n, lap=3):
    best_time = float('inf')
    for _ in range(lap):
        t0 = perf_counter()
        thuat_toan_o_n2(n)
        t1 = perf_counter()
        best_time = min(best_time, t1 - t0)
    return best_time
sizes = [500, 1000, 2000, 4000]
times = []
for idx, n in enumerate(sizes):
    t = do_thoi_gian(n)
    times.append(t)
    if idx == 0:
        print(f"n = {n} -> Thoi gian min: {t:.5f} s")
    else:
        ratio = t / times[idx - 1]
        print(f"n = {n} -> Thoi gian min: {t:.5f} s | Ti le: {ratio:.5f}")