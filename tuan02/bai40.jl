using Printf

function kadane_chi_so(a::Vector{Int})
    n = length(a)
    if n == 0
        return (0, 0, 0)
    end
    best = a[1]; cur = a[1]
    l = 1; r = 1; bat_dau = 1
    for i in 2:n
        if cur + a[i] >= a[i]
            cur = cur + a[i]
        else
            cur = a[i]
            bat_dau = i
        end
        if cur > best
            best = cur
            l = bat_dau
            r = i
        end
    end
    return (best, l, r)
end
function main()
    input_data = split(read(stdin, String))
    if isempty(input_data)
        return
    end
    n = parse(Int, input_data[1])
    a = [parse(Int, input_data[i + 1]) for i in 1:n]
    best, l, r = kadane_chi_so(a)
    @printf("tong %d, doan [%d..%d]\n", best, l, r)
end
main()