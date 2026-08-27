using Printf
function thong_ke(a)
    tong = sum(a)
    trung_binh = tong / length(a)
    nho_nhat = minimum(a)
    lon_nhat = maximum(a)
    return tong, trung_binh, nho_nhat, lon_nhat
end
function main()
    input_data = split(read(stdin, String))
    if isempty(input_data)
        return
    end
    n = parse(Int64, input_data[1])
    a = [parse(Int64, x) for x in input_data[2:n+1]]
    
    tong, trung_binh, nho_nhat, lon_nhat = thong_ke(a)
    @printf("%d %.4f %d %d\n", tong, trung_binh, nho_nhat, lon_nhat)
end
main()