using Random
using Printf

function cua_so_truot(a::Vector{Int}, k::Int)
    current_sum = sum(a[1:k])
    max_sum = current_sum
    start_idx = 1
    for i in (k + 1):length(a)
        current_sum += a[i] - a[i - k]
        if current_sum > max_sum
            max_sum = current_sum
            start_idx = i - k + 1
        end
    end
    return (max_sum, start_idx)
end
function cua_so_truot_ngay_tho(a::Vector{Int}, k::Int)
    max_sum = typemin(Int64)
    for i in 1:(length(a) - k + 1)
        s = 0
        for j in i:(i + k - 1) s += a[j] end
        if s > max_sum max_sum = s end
    end
end
function do_thoi_gian()
    n, k = 1000000, 1000
    a = rand(-100:100, n)
    t1 = time()
    cua_so_truot_ngay_tho(a, k)
    t_naive = time() - t1
    t3 = time()
    cua_so_truot(a, k)
    t_window = time() - t3
    @printf("[Do thoi gian n=10^6, k=1000] Julia | O(n*k): %.4fs | O(n): %.4fs | Nhanh hon: %.2fx\n", t_naive, t_window, t_naive / t_window)
end
function main()
    data = split(read(stdin, String))
    if isempty(data) return end
    n = parse(Int, data[1])
    k = parse(Int, data[2])
    a = [parse(Int, data[i+2]) for i in 1:n]
    tong, vi_tri = cua_so_truot(a, k)
    println("tong $tong, bat dau tai vi tri $vi_tri")
    do_thoi_gian()
end
main()