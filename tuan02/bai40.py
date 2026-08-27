import sys

def kadane_chi_so(a):
    n = len(a)
    if n == 0:
        return 0, 0, 0
    best = cur = a[0]
    l = r = bat_dau = 0
    for i in range(1, n):
        if cur + a[i] >= a[i]:
            cur = cur + a[i]
        else:
            cur = a[i]
            bat_dau = i
        if cur > best:
            best, l, r = cur, bat_dau, i
    return best, l + 1, r + 1 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(v) for v in input_data[1:n + 1]]
    best, l, r = kadane_chi_so(a)
    print(f"tong {best}, doan [{l}..{r}]")
if __name__ == "__main__":
    main()