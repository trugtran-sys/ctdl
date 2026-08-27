function dao_nguoc(n::Int)
    sign_val = n < 0 ? -1 : 1
    temp = abs(n)
    res = 0
    while temp > 0
        res = res * 10 + temp % 10
        temp = div(temp, 10)
    end
    return res * sign_val
end
function main()
    line = readline()
    if !isempty(strip(line))
        n = parse(Int, strip(line))
        println(dao_nguoc(n))
    end
end
main()