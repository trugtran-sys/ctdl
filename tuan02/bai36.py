import math
import sys

LLONG_MAX = 9223372036854775807
def giai_thua(n: int) -> int:
    if n < 0:
        return -1
    return math.factorial(n)
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        kq = giai_thua(n)
        if kq <= LLONG_MAX:
            print(kq)
        else:
            print(f"TRAN SO ({n}! = {kq} > {LLONG_MAX})")