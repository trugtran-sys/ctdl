using Random
using Printf

function cach1(a)
    n = length(a)
    max_sum = typemin(Int64)
    for i in 1:n
        for j in i:n
            s = sum(a[i:j])
            if s > max_sum
                max_sum = s
            end
        end
    end
    return max_sum
end
function cach2(a)
    n = length(a)
    max_sum = typemin(Int64)
    for i in 1:n
        s = 0
        for j in i:n
            s += a[j]
            if s > max_sum
                max_sum = s
            end
        end
    end
    return max_sum
end
function kadane(a)
    max_so_far = a[1]
    curr_max = a[1]
    for i in 2:lastindex(a)
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    end
    return max_so_far
end
function do_thoi_gian()
    sizes = [200, 400, 800]
    for c in 1:3
        times = Float64[]
        for n in sizes
            rng = MersenneTwister(42)
            a = rand(rng, -100:100, n)
            runs = (c == 1) ? 5 : ((c == 2) ? 1000 : 200000)
            start_time = time_ns()
            for r in 1:runs
                if c == 1
                    cach1(a)
                elseif c == 2
                    cach2(a)
                else
                    kadane(a)
                end
            end
            end_time = time_ns()
            diff = (end_time - start_time) / 1e9
            push!(times, diff / runs)
        end
        @printf("%.6f %.6f %.6f\n", times[1], times[2], times[3])
    end
end
function main()
    tokens = Int[]
    for line in eachline(stdin)
        if !isempty(strip(line))
            parsed_line = [parse(Int, x) for x in split(line)]
            append!(tokens, parsed_line)
        end
    end
    idx = 1
    while idx <= length(tokens)
        n = tokens[idx]
        idx += 1
        if n == 0
            do_thoi_gian()
        else
            a = tokens[idx : idx + n - 1]
            idx += n
            println(kadane(a))
        end
    end
end
if abspath(PROGRAM_FILE) == @__FILE__
    main()
end