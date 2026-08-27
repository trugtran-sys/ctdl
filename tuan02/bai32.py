import sys

def la_chinh_phuong(n: int) -> bool:
    if n < 0:
        return False
    left, right = 0, 10**9
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return True
        if sq < n:
            left = mid + 1
        else:
            right = mid - 1
    return False
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        if la_chinh_phuong(n):
            print("YES")
        else:
            print("NO")