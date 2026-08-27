import sys

GIOI_HAN_DE_QUY = 35
MAX_INT64 = 2**63 - 1
dem_goi = 0
def fib_de_quy(n):
    global dem_goi
    dem_goi += 1
    if n <= 2: return 1
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)
def fib_ghi_nho(n, mem):
    if n <= 2: return 1
    if n in mem: return mem[n]
    mem[n] = fib_ghi_nho(n - 1, mem) + fib_ghi_nho(n - 2, mem)
    return mem[n]
def fib_lap(n):
    if n <= 2: return True, 1
    f1, f2 = 1, 1
    for _ in range(3, n + 1):
        if f2 > MAX_INT64 - f1: return False, 0
        f1, f2 = f2, f1 + f2
    return True, f2
def main():
    inp = sys.stdin.read().split()
    if not inp: return
    n = int(inp[0])
    print(f"n = {n}")
    ok, kq_lap = fib_lap(n)
    if not ok:
        print(f"Loi: F_{n} vuot qua kieu long long (F_92 la max)")
        return
    if n <= GIOI_HAN_DE_QUY:
        global dem_goi
        dem_goi = 0
        kq_dq = fib_de_quy(n)
        print(f"De quy thuan: F = {kq_dq}, so loi goi = {dem_goi}")
    else:
        uoc_luong = 2.0 * kq_lap - 1
        print(f"De quy thuan: Bo qua (uoc tinh co {uoc_luong:.2e} loi goi, qua lau)")
    print(f"Ghi nho     : F = {fib_ghi_nho(n, {})}")
    print(f"Vong lap    : F = {kq_lap}")
if __name__ == "__main__":
    main()