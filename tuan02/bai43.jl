using Printf

const GIOI_HAN_DE_QUY = 35
const DEM = Ref(0)
const MAX_INT64 = typemax(Int64)
function fib_de_quy(n::Int)
    DEM[] += 1
    if n <= 2 return 1 end
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)
end
function fib_ghi_nho(n::Int, mem::Dict{Int, Int64})
    if n <= 2 return 1 end
    if haskey(mem, n) return mem[n] end
    mem[n] = fib_ghi_nho(n - 1, mem) + fib_ghi_nho(n - 2, mem)
    return mem[n]
end
function fib_lap(n::Int)
    if n <= 2 return (true, Int64(1)) end
    f1::Int64, f2::Int64 = 1, 1
    for i in 3:n
        if f2 > MAX_INT64 - f1 return (false, Int64(0)) end
        f1, f2 = f2, f1 + f2
    end
    return (true, f2)
end
function main()
    inp = split(read(stdin, String))
    if isempty(inp) return end
    n = parse(Int, inp[1])
    println("n = $n")
    ok, kq_lap = fib_lap(n)
    if !ok
        println("Loi: F_$n vuot qua kieu long long (F_92 la max)")
        return
    end
    if n <= GIOI_HAN_DE_QUY
        DEM[] = 0
        kq_dq = fib_de_quy(n)
        println("De quy thuan: F = $kq_dq, so loi goi = ", DEM[])
    else
        uoc_luong = 2.0 * kq_lap - 1
        @printf("De quy thuan: Bo qua (uoc tinh co %.2e loi goi, qua lau)\n", uoc_luong)
    end
    println("Ghi nho     : F = ", fib_ghi_nho(n, Dict{Int, Int64}()))
    println("Vong lap    : F = $kq_lap")
end
main()