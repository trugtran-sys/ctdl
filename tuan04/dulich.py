matrix = [
    [0, 10, 9, 22, 23],
    [10, 0, 16, 19, 14],
    [9, 16, 0, 7, 28],
    [22, 19, 7, 0, 8],
    [23, 14, 28, 8, 0]
]
n, c_min = 5, 7
def solve(step, u, cur_cost, use_bound, path):
    global nodes, best_cost, best_path
    nodes += 1
    if use_bound and cur_cost + (n - step + 1) * c_min >= best_cost:
        return
    if step == n:
        if cur_cost + matrix[u][0] < best_cost:
            best_cost = cur_cost + matrix[u][0]
            best_path = path + [0]
        return
    for v in range(1, n):
        if not visited[v]:
            visited[v] = True
            solve(step + 1, v, cur_cost + matrix[u][v], use_bound, path + [v])
            visited[v] = False
for mode, use_bound in [("KHONG", False), ("CO", True)]:
    nodes, best_cost, best_path = 0, float('inf'), []
    visited = [False] * n
    visited[0] = True
    solve(1, 0, 0, use_bound, [0])
    path_str = " -> ".join(map(str, best_path))
    print(f"{mode} cat nhanh: Cost = {best_cost}, Nodes = {nodes}, Path = {path_str}")