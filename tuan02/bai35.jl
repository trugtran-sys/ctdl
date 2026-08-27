function la_nguyen_to(n::Int)
    if n < 2 return false end
    for i in 2:isqrt(n)
        if n % i == 0 return false end
    end
    return true
end
function sang(n::Int)
    if n < 2 return Int[] end
    is_prime = fill(true, n)
    is_prime[1] = false
    for p in 2:isqrt(n)
        if is_prime[p]
            for i in (p*p):p:n
                is_prime[i] = false
            end
        end
    end
    return findall(is_prime)
end
function main()
    line = readline()
    if !isempty(strip(line))
        n = parse(Int, strip(line))
        t_tung_so = @elapsed begin
            cnt = 0
            for i in 2:n
                if la_nguyen_to(i) cnt += 1 end
            end
        end
        primes = Int[]
        t_sang = @elapsed begin
            primes = sang(n)
        end
        if n == 30
            println(join(primes, " "), " ($(length(primes)) số)")
        elseif n == 1000000
            println("so luong = $(length(primes)), tong = $(sum(Int64, primes))")
        else
            println("so luong = $(length(primes))")
        end
        println("Thoi gian: Tung so = $(round(t_tung_so, digits=4))s | Sang = $(round(t_sang, digits=4))s")
    end
end
main()