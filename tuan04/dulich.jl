const INF = 10^9
matrix = [
    0  10   9  22  23;
   10   0  16  19  14;
    9  16   0   7  28;
   22  19   7   0   8;
   23  14  28   8   0
]
n = size(matrix, 1)
c_min = 7
global nodes = 0; global best_cost = INF; global best_path = Int[]
function solve(step, u, cur_cost, use_bound, path, visited)
    global nodes, best_cost, best_path
    nodes += 1
    if use_bound && cur_cost + (n - step + 1) * c_min >= best_cost
        return
    end
    if step == n
        if cur_cost + matrix[u, 1] < best_cost
            best_cost = cur_cost + matrix[u, 1]
            best_path = copy(path)
            push!(best_path, 1)
        end
        return
    end
    for v in 2:n
        if !visited[v]
            visited[v] = true
            push!(path, v)
            solve(step + 1, v, cur_cost + matrix[u, v], use_bound, path, visited)
            pop!(path)
            visited[v] = false
        end
    end
end
for (mode, use_bound) in [("KHONG", false), ("CO", true)]
    global nodes = 0; global best_cost = INF; global best_path = Int[]
    visited = falses(n)
    visited[1] = true
    solve(1, 1, 0, use_bound, [1], visited)
    println("$mode cat nhanh: Cost = $best_cost, Nodes = $nodes, Path = $best_path")
end