function main()
    data = split(read(stdin, String))
    if isempty(data) return end
    n = parse(Int64, data[1])
    a = [parse(Int64, x) for x in data[2:n+1]]
    println("$(sum(a)) $(maximum(a))")
end
main()