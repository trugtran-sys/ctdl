const global_dummy = Ref{Int}(0)
function thuat_toan_o_n2(n)
    tong = 0
    for i in 1:n
        for j in 1:n
            tong += i + j
        end
    end
    return tong
end
thuat_toan_o_n2(10)
sizes = [500, 1000, 2000, 4000]
times = Float64[]
for (idx, n) in enumerate(sizes)
    min_t = Inf
    for _ in 1:3
        t0 = time_ns()
        res = thuat_toan_o_n2(n)
        t1 = time_ns()
        global_dummy[] = res 
        sec = Float64(t1 - t0) / 1e9
        if sec < min_t
            min_t = sec
        end
    end
    push!(times, min_t)
    if idx == 1
        println("n = $n -> Thoi gian min: $min_t s")
    else
        ratio = min_t / times[idx - 1]
        println("n = $n -> Thoi gian min: $min_t s | Ti le: $ratio")
    end
end