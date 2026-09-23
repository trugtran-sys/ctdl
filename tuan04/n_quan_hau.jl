function giai_n_hau()
    print("Nhập n: ")
    n = parse(Int, readline())
    so_nut = Ref(0)
    so_loi_giai = Ref(0)
    first_sol = Ref(Int[])
    x = zeros(Int, n)
    cot = fill(true, n)
    cheo1 = fill(true, 2n)
    cheo2 = fill(true, 2n)
    function backtrack(i)
        so_nut[] += 1
        if i > n
            so_loi_giai[] += 1
            if isempty(first_sol[])
                first_sol[] = copy(x)
            end
            return
        end
        for j in 1:n
            c1 = i - j + n
            c2 = i + j - 1
            if cot[j] && cheo1[c1] && cheo2[c2]
                x[i] = j
                cot[j] = cheo1[c1] = cheo2[c2] = false
                backtrack(i + 1)
                cot[j] = cheo1[c1] = cheo2[c2] = true
            end
        end
    end
    backtrack(1)
    println("Số nút đã duyệt: ", so_nut[])
    println("Số lời giải: ", so_loi_giai[])
    println("Bàn cờ lời giải đầu tiên (x): ", first_sol[])
end
giai_n_hau()