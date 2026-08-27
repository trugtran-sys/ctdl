function da_sap_xep(a; nghiem_ngat=false)
    for i in 1:length(a)-1
        if nghiem_ngat
            if a[i] >= a[i+1]
                return false
            end
        else
            if a[i] > a[i+1]
                return false
            end
        end
    end
    return true
end
function main()
    input_text = read(stdin, String)
    tokens = split(input_text)
    if !isempty(tokens)
        n = parse(Int, tokens[1])
        a = [parse(Int, tokens[i]) for i in 2:n+1]
        nn = da_sap_xep(a, nghiem_ngat=true)
        kg = da_sap_xep(a, nghiem_ngat=false)
        res_nn = nn ? "YES" : "NO"
        res_kg = kg ? "YES" : "NO"
        println("$res_nn - $res_kg")
    end
end
main()