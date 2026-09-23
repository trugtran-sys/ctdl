import sys

def linear_search(a, target):
    comparisons = 0
    for i, value in enumerate(a):
        comparisons += 1  # Chi dem phep so sanh value == target.
        if value == target:
            return i, comparisons
    return -1, comparisons

def solve(a, target):
    n = len(a)
    total = 0
    smallest = largest = None
    for value in a:
        total += value
        if smallest is None or value < smallest:
            smallest = value
        if largest is None or value > largest:
            largest = value
    first, comparisons = linear_search(a, target)
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            pairs += 1  # Thuc su duyet tung cap; khong thay bang cong thuc.
    doublings = 0
    size = 1
    while size <= n:
        doublings += 1
        size *= 2
    return total, smallest, largest, first, comparisons, pairs, doublings

def main():
    tokens = list(map(int, sys.stdin.read().split()))
    n = tokens[0]
    a, target = tokens[1:1 + n], tokens[1 + n]
    total, low, high, first, cmps, pairs, doubles = solve(a, target)
    print("SUM", total)
    print("MIN", "NA" if low is None else low)
    print("MAX", "NA" if high is None else high)
    print("FIRST", first)
    print("SEARCH_CMPS", cmps)
    print("PAIRS", pairs)
    print("DOUBLINGS", doubles)
    print("SCAN_VISITS", n)

if __name__ == "__main__":
    main()
