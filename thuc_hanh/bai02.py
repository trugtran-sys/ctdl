import sys

def insertion_sort(a):
    comparisons = shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1  # Chi dem so sanh gia tri, ke ca lan sai.
            if a[j] <= key:
                break  # Khong day phan tu bang key: giu tinh on dinh.
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key  # Lan dat key nay khong tinh vao shifts.
    return comparisons, shifts

def merge_sort(a):
    buffer = [0] * len(a)  # Dung lai mot bo dem cho toan bo de quy.
    comparisons = 0

    def visit(lo, hi):
        nonlocal comparisons
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        visit(lo, mid)
        visit(mid + 1, hi)
        i, j, out = lo, mid + 1, lo
        while i <= mid and j <= hi:
            comparisons += 1
            if a[i] <= a[j]:  # Bang nhau: lay ben trai truoc.
                buffer[out] = a[i]
                i += 1
            else:
                buffer[out] = a[j]
                j += 1
            out += 1
        while i <= mid:
            buffer[out] = a[i]
            i, out = i + 1, out + 1
        while j <= hi:
            buffer[out] = a[j]
            j, out = j + 1, out + 1
        for pos in range(lo, hi + 1):
            a[pos] = buffer[pos]

    visit(0, len(a) - 1)
    return comparisons

def main():
    tokens = list(map(int, sys.stdin.read().split()))
    n = tokens[0]
    a = tokens[1:1 + n]
    insertion = a.copy()
    merge = a.copy()
    cmps, shifts = insertion_sort(insertion)
    merge_cmps = merge_sort(merge)
    print("INSERT", *insertion)
    print("INSERT_CMPS", cmps)
    print("INSERT_SHIFTS", shifts)
    print("MERGE", *merge)
    print("MERGE_CMPS", merge_cmps)

if __name__ == "__main__":
    main()