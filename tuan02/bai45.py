import sys
def luy_thua_mod(a: int, b: int, m: int) -> int:
    r = 1 % m
    a = a % m
    while b > 0:
        if b % 2 == 1:
            r = (r * a) % m
        a = (a * a) % m
        b //= 2
    return r
if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            a, b, m = map(int, line.split())
            print(luy_thua_mod(a, b, m))