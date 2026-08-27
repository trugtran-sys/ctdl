function phan_tich(n::Int)
    if n == 0
        return (1, 0)
    end
    so_chu_so = 0
    tong_chu_so = 0
    while n > 0
        tong_chu_so += n % 10
        so_chu_so += 1
        n = div(n, 10)
    end
    return (so_chu_so, tong_chu_so)
end
function main()
    line = readline()
    if !isempty(strip(line))
        n = parse(Int, strip(line))
        so_cs, tong_cs = phan_tich(n)
        println("$so_cs $tong_cs")
    end
end
main()