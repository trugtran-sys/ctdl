function dem(a)
    chan = count(x -> x % 2 == 0, a)
    le = count(x -> x % 2 != 0, a)
    am = count(x -> x != 0 && x % 2 != 0, a) 
    chan_cnt = count(x -> x % 2 == 0, a)
    le_cnt = count(x -> x % 2 != 0, a)
    am_cnt = count(x -> x < 0, a)
    return (chan_cnt, le_cnt, am_cnt)
end
function main()
    input_text = read(stdin, String)
    tokens = split(input_text)
    if !isempty(tokens)
        n = parse(Int, tokens[1])
        a = [parse(Int, tokens[i]) for i in 2:n+1]
        chan, le, am = dem(a)
        println("chan $chan, le $le, am $am")
    end
end
main()