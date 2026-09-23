struct Item
    name::String
    v::Int
    w::Int
    vw::Float64
end
items = [
    Item("A", 19, 4, 19/4), Item("B", 25, 7, 25/7), 
    Item("C", 7, 3, 7/3), Item("D", 8, 3, 8/3), 
    Item("E", 9, 3, 9/3), Item("F", 21, 10, 21/10)
]
sort!(items, by = x -> x.vw, rev = true)
n, W = length(items), 14
global best_v = 0; global nodes = 0; global best_subset = String[]
function calc_bound(i, cur_w, cur_v)
    if cur_w >= W; return 0.0; end
    profit = Float64(cur_v); totw = cur_w; j = i
    while j <= n && totw + items[j].w <= W
        totw += items[j].w
        profit += items[j].v
        j += 1
    end
    if j <= n; profit += (W - totw) * items[j].vw; end
    return profit
end
function solve(i, cur_w, cur_v, use_bound, cur_subset)
    global nodes, best_v, best_subset
    nodes += 1
    if cur_v > best_v
        best_v = cur_v; best_subset = copy(cur_subset)
    end
    if i > n; return; end
    if use_bound && calc_bound(i, cur_w, cur_v) <= best_v; return; end
    if cur_w + items[i].w <= W
        push!(cur_subset, items[i].name)
        solve(i + 1, cur_w + items[i].w, cur_v + items[i].v, use_bound, cur_subset)
        pop!(cur_subset)
    end
    solve(i + 1, cur_w, cur_v, use_bound, cur_subset)
end
solve(1, 0, 0, false, String[])
println("KHONG cat nhanh: Max = $best_v, Nodes = $nodes")
global nodes = 0; global best_v = 0; global best_subset = String[]
solve(1, 0, 0, true, String[])
println("CO cat nhanh: Max = $best_v, Nodes = $nodes")