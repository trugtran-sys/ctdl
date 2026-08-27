function luy_thua_mod(a::Int, b::Int, m::Int)
    r = 1 % m
    a = a % m
    while b > 0
        if b % 2 == 1
            r = (r * a) % m
        end
        a = (a * a) % m
        b ÷= 2
    end
    return r
end
for line in eachline(stdin)
    if !isempty(strip(line))
        parts = parse.(Int, split(line))
        println(luy_thua_mod(parts[1], parts[2], parts[3]))
    end
end