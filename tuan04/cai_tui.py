class Item:
    def __init__(self, name, v, w):
        self.name = name; self.v = v; self.w = w
        self.vw = v / w
items = [Item('A', 19, 4), Item('B', 25, 7), Item('C', 7, 3), 
         Item('D', 8, 3), Item('E', 9, 3), Item('F', 21, 10)]
items.sort(key=lambda x: x.vw, reverse=True)
n, W = len(items), 14
def bound(i, cur_w, cur_v):
    if cur_w >= W: return 0
    profit = cur_v; totw = cur_w
    j = i
    while j < n and totw + items[j].w <= W:
        totw += items[j].w
        profit += items[j].v
        j += 1
    if j < n:
        profit += (W - totw) * items[j].vw
    return profit
def solve(i, cur_w, cur_v, use_bound, cur_subset):
    global nodes, best_v, best_subset
    nodes += 1
    if cur_v > best_v:
        best_v = cur_v
        best_subset = cur_subset[:]
    if i == n: return
    if use_bound and bound(i, cur_w, cur_v) <= best_v: return
    if cur_w + items[i].w <= W:
        cur_subset.append(items[i].name)
        solve(i + 1, cur_w + items[i].w, cur_v + items[i].v, use_bound, cur_subset)
        cur_subset.pop()
    solve(i + 1, cur_w, cur_v, use_bound, cur_subset)
for mode, use_bound in [("KHONG", False), ("CO", True)]:
    nodes, best_v, best_subset = 0, 0, []
    solve(0, 0, 0, use_bound, [])
    print(f"{mode} cat nhanh: Max Value = {best_v}, Nodes = {nodes}, Items = {best_subset}")