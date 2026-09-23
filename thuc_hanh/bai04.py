import sys
def merge_neighbors(a):
    buffer = [None] * len(a)

    def visit(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        visit(lo, mid)
        visit(mid + 1, hi)
        i, j, out = lo, mid + 1, lo
        while i <= mid and j <= hi:
            # Ban ghi la (distance_squared, id, label).
            # So sanh hai khoa dau, khong dung nhan de xep hang.
            if a[i][:2] <= a[j][:2]:
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
def classify(records, query, k):
    neighbors = []
    qx, qy = query
    for identity, x, y, label in records:
        distance = (x - qx) ** 2 + (y - qy) ** 2
        neighbors.append((distance, identity, label))
    merge_neighbors(neighbors)
    chosen = neighbors[:k]
    votes_a = sum(row[2] == "A" for row in chosen)
    votes_b = k - votes_a
    prediction = "A" if votes_a >= votes_b else "B"
    return chosen, votes_a, votes_b, prediction
def main():
    tokens = sys.stdin.read().split()
    n, k = map(int, tokens[:2])
    if not (1 <= n <= 2000 and 1 <= k <= n):
        print("ERROR: invalid data")
        return 1
    records = []
    ids = set()
    for i in range(n):
        pos = 2 + 4 * i
        identity, x, y = map(int, tokens[pos:pos + 3])
        label = tokens[pos + 3]
        if (identity in ids or not 1 <= identity <= 1000000
                or not 0 <= x <= 10 or not 0 <= y <= 10
                or label not in ("A", "B")):
            print("ERROR: invalid data")
            return 1
        ids.add(identity)
        records.append((identity, x, y, label))
    query = tuple(map(int, tokens[2 + 4 * n:4 + 4 * n]))
    if any(value < 0 or value > 10 for value in query):
        print("ERROR: invalid data")
        return 1
    chosen, votes_a, votes_b, prediction = classify(records, query, k)
    print("NEIGHBORS", k)
    for distance, identity, label in chosen:
        print(identity, label, distance)
    print("VOTES A", votes_a, "B", votes_b)
    print("PREDICT", prediction)
    return 0
if __name__ == "__main__":
    sys.exit(main())