struct Activity
    name::String
    s::Int
    f::Int
end
function get_overlaps(activities)
    overlaps = Dict{String, Int}()
    for act in activities; overlaps[act.name] = 0; end
    n = length(activities)
    for i in 1:n
        for j in (i+1):n
            if !(activities[i].f <= activities[j].s || activities[j].f <= activities[i].s)
                overlaps[activities[i].name] += 1
                overlaps[activities[j].name] += 1
            end
        end
    end
    return overlaps
end
function is_compatible(selected, new_act)
    for act in selected
        if !(new_act.f <= act.s || act.f <= new_act.s)
            return false
        end
    end
    return true
end
function greedy_criteria(activities)
    acts_finish = sort(activities, by = x -> (x.f, x.s))
    res_finish = Activity[]
    last_finish = -1
    for act in acts_finish
        if act.s >= last_finish
            push!(res_finish, act)
            last_finish = act.f
        end
    end
    acts_start = sort(activities, by = x -> (x.s, x.f))
    res_start = Activity[]
    last_f = -1
    for act in acts_start
        if act.s >= last_f
            push!(res_start, act)
            last_f = act.f
        end
    end
    acts_short = sort(activities, by = x -> (x.f - x.s, x.s))
    res_short = Activity[]
    for act in acts_short
        if is_compatible(res_short, act)
            push!(res_short, act)
        end
    end
    overlaps = get_overlaps(activities)
    acts_overlap = sort(activities, by = x -> (overlaps[x.name], x.s))
    res_overlap = Activity[]
    for act in acts_overlap
        if is_compatible(res_overlap, act)
            push!(res_overlap, act)
        end
    end
    return res_finish, res_start, res_short, res_overlap
end
function dynamic_programming_max(activities)
    acts = sort(activities, by = x -> x.f)
    n = length(acts)
    if n == 0 return 0 end
    dp = ones(Int, n)
    for i in 2:n
        for j in 1:(i-1)
            if acts[j].f <= acts[i].s
                dp[i] = max(dp[i], dp[j] + 1)
            end
        end
    end
    return maximum(dp)
end
function main()
    std_data = [
        Activity("H1", 1, 5), Activity("H2", 2, 5), Activity("H3", 2, 6), Activity("H4", 3, 4), Activity("H5", 4, 8),
        Activity("H6", 6, 9), Activity("H7", 8, 11), Activity("H8", 9, 14), Activity("H9", 11, 13), Activity("H10", 12, 15)
    ]
    rf, rs, rsh, ro = greedy_criteria(std_data)
    true_max = dynamic_programming_max(std_data)
    println("1. Ket thuc som nhat: ", [a.name for a in rf], " (So HĐ: ", length(rf), ")")
    println("2. Bat dau som nhat : ", [a.name for a in rs], " (So HĐ: ", length(rs), ")")
    println("3. Ngan nhat        : ", [a.name for a in rsh], " (So HĐ: ", length(rsh), ")")
    println("4. It chong lan nhat: ", [a.name for a in ro], " (So HĐ: ", length(ro), ")")
    println("=> So nhieu nhat that su (DP): ", true_max)
    rand_data = Activity[]
    for i in 1:7
        s = rand(1:10)
        f = s + rand(1:5)
        push!(rand_data, Activity("R$i", s, f))
    end
    dp_max_rand = dynamic_programming_max(rand_data)
    rf_rand, _, _, _ = greedy_criteria(rand_data)
    println("Du lieu ngau nhien sinh 7 hoat dong.")
    println("Quy hoach dong (Toi uu): ", dp_max_rand)
    println("Tham lam ket thuc som: ", length(rf_rand))
end
main()