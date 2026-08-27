const LLONG_MAX = typemax(Int64)
function giai_thua(n::Int)
    if n < 0 return -1 end
    return factorial(big(n))
end
function main()
    line = readline()
    if !isempty(strip(line))
        n = parse(Int, strip(line))
        kq = giai_thua(n)
        if kq <= LLONG_MAX
            println(kq)
        else
            println("TRAN SO ($(n)! = $kq > $LLONG_MAX)")
        end
    end
end
main()