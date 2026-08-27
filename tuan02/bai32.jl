function la_chinh_phuong(n::Int)
    if n < 0
        return false
    end
    left, right = Int128(0), Int128(10^9)
    while left <= right
        mid = div(left + right, 2)
        sq = mid * mid
        if sq == n
            return true
        elseif sq < n
            left = mid + 1
        else
            right = mid - 1
        end
    end
    return false
end
function main()
    line = readline()
    if !isempty(line)
        n = parse(Int, strip(line))
        if la_chinh_phuong(n)
            println("YES")
        else
            println("NO")
        end
    end
end
main()