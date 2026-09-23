import sys
def bound(a, target, upper=False):
    lo, hi = 0, len(a)  # Khoang ung vien [lo, hi); hi duoc phep bang n.
    probes = 0
    while lo < hi:
        mid = lo + (hi - lo) // 2
        probes += 1
        move_right = a[mid] <= target if upper else a[mid] < target
        if move_right:
            lo = mid + 1
        else:
            hi = mid
    return lo, probes
def main():
    tokens = list(map(int, sys.stdin.read().split()))
    n = tokens[0]
    a, target = tokens[1:1 + n], tokens[1 + n]
    if any(a[i] > a[i + 1] for i in range(n - 1)):
        print("ERROR: array must be sorted")
        return 1
    lower, p1 = bound(a, target)
    upper, p2 = bound(a, target, upper=True)
    first = lower if lower < n and a[lower] == target else -1
    print("FIRST", first)
    print("COUNT", upper - lower)
    print("LOWER", lower)
    print("UPPER", upper)
    print("PROBES", p1 + p2)
    return 0
if __name__ == "__main__":
    sys.exit(main())