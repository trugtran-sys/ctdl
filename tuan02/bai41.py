import sys

def tich_lon_nhat(a):
    if not a:
        return 0
    best = max_end = min_end = a[0]
    for val in a[1:]:
        if val < 0:
            max_end, min_end = min_end, max_end
        max_end = max(val, max_end * val)
        min_end = min(val, min_end * val)
        best = max(best, max_end)
    return best
def tich_lon_nhat_n2(a):
    if not a:
        return 0
    best = a[0]
    for i in range(len(a)):
        cur = 1
        for j in range(i, len(a)):
            cur *= a[j]
            if cur > best:
                best = cur
    return best
def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    a = [int(v) for v in input_data[1:n+1]]
    print(tich_lon_nhat(a))
if __name__ == "__main__":
    main()