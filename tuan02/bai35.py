import math
import sys
import time

def la_nguyen_to(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def sang(n: int) -> list:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        t0 = time.perf_counter()
        cnt = sum(1 for i in range(2, n + 1) if la_nguyen_to(i))
        t_tung_so = time.perf_counter() - t0
        t0 = time.perf_counter()
        primes = sang(n)
        t_sang = time.perf_counter() - t0
        if n == 30:
            print(" ".join(map(str, primes)) + f" ({len(primes)} số)")
        elif n == 1000000:
            print(f"so luong = {len(primes)}, tong = {sum(primes)}")
        else:
            print(f"so luong = {len(primes)}")
        print(f"Thoi gian: Tung so = {t_tung_so:.4f}s | Sang = {t_sang:.4f}s")