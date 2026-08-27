function tich_lon_nhat(a::Vector{Int})
    if isempty(a)
        return 0
    end
    best = a[1]; max_end = a[1]; min_end = a[1]
    for i in 2:length(a)
        val = a[i]
        if val < 0
            max_end, min_end = min_end, max_end
        end
        max_end = max(val, max_end * val)
        min_end = min(val, min_end * val)
        best = max(best, max_end)
    end
    return best
end
function tich_lon_nhat_n2(a::Vector{Int})
    if isempty(a)
        return 0
    end
    best = a[1]
    for i in 1:length(a)
        cur = 1
        for j in i:length(a)
            cur *= a[j]
            if cur > best
                best = cur
            end
        end
    end
    return best
end
function main()
    input_data = split(read(stdin, String))
    if isempty(input_data) return end
    
    n = parse(Int, input_data[1])
    a = [parse(Int, input_data[i+1]) for i in 1:n]
    println(tich_lon_nhat(a))
end
main()