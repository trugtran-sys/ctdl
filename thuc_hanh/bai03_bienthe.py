import sys

def bound(a, target, upper=False):
    lo, hi = 0, len(a)  
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
    
    a = tokens[1:1 + n]
    L = tokens[1 + n]
    R = tokens[2 + n]
    
    if any(a[i] > a[i + 1] for i in range(n - 1)):
        print("ERROR: array must be sorted")
        return 1
    if L > R:
        print("COUNT 0")
        return 0
        
    lower, p1 = bound(a, L, upper=False)
    upper, p2 = bound(a, R, upper=True)
    
    print("COUNT", upper - lower)
    print("PROBES", p1 + p2)
    return 0

if __name__ == "__main__":
    sys.exit(main())