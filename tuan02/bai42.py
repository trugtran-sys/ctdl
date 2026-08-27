import sys
import time
import random

def cua_so_truot(a, k):
    current_sum = sum(a[:k])
    max_sum = current_sum
    start_idx = 0
    for i in range(k, len(a)):
        current_sum += a[i] - a[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx = i - k + 1
    return max_sum, start_idx + 1
def cua_so_truot_ngay_tho(a, k):
    max_sum = -float('inf')
    for i in range(len(a) - k + 1):
        s = sum(a[i:i+k])
        if s > max_sum: max_sum = s
def do_thoi_gian():
    n, k = 1000000, 1000
    a = [random.randint(-100, 100) for _ in range(n)]
    t1 = time.time()
    cua_so_truot_ngay_tho(a, k)
    t_naive = time.time() - t1
    t3 = time.time()
    cua_so_truot(a, k)
    t_window = time.time() - t3
    print(f"[Do thoi gian n=10^6, k=1000] Python | O(n*k): {t_naive:.4f}s | O(n): {t_window:.4f}s | Nhanh hon: {t_naive/t_window:.2f}x")
def main():
    data = sys.stdin.read().split()
    if not data: return
    n, k = int(data[0]), int(data[1])
    a = [int(v) for v in data[2:n+2]]
    tong, vi_tri = cua_so_truot(a, k)
    print(f"tong {tong}, bat dau tai vi tri {vi_tri}")
    do_thoi_gian()
if __name__ == "__main__":
    main()