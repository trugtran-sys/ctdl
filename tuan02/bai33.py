import sys

def phan_tich(n: int):
    if n == 0:
        return (1, 0)
    so_chu_so = 0
    tong_chu_so = 0
    while n > 0:
        tong_chu_so += n % 10
        so_chu_so += 1
        n //= 10
    return (so_chu_so, tong_chu_so)
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        so_cs, tong_cs = phan_tich(n)
        print(f"{so_cs} {tong_cs}")