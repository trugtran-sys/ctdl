import sys

def dao_nguoc(n: int) -> int:
    sign = -1 if n < 0 else 1
    temp = abs(n)
    res = 0
    while temp > 0:
        res = res * 10 + temp % 10
        temp //= 10
    return res * sign
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        print(dao_nguoc(n))