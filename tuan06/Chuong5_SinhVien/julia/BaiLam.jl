module BaiLam
using ..CauTruc
const BAN = "Sinh viên"
export dem_gia_tri, xoa_tat_ca!, lay_nhieu!, xem_k

struct ChuaHoanThanh <: Exception
    msg::String
end
Base.showerror(io::IO, e::ChuaHoanThanh) = print(io, e.msg)

"""Duyệt ke để đếm nút có gt == x. Không thay đổi L."""
function dem_gia_tri(L::DSLK, x)
    count = 0
    p = L.dau
    while p !== nothing
        if p.gt == x
            count += 1
        end
        p = p.ke
    end
    return count
end

"""Một lượt duyệt; xoá mọi nút có gt == x; cập nhật n; trả số nút đã xoá."""
function xoa_tat_ca!(L::DSLK, x)
    count = 0
    truoc = nothing
    p = L.dau
    while p !== nothing
        if p.gt == x
            if truoc === nothing
                L.dau = p.ke
            else
                truoc.ke = p.ke
            end
            p = p.ke
            count += 1
            L.n -= 1
        else
            truoc = p
            p = p.ke
        end
    end
    return count
end

"""Lấy đúng k giá trị LIFO. k sai phải báo ArgumentError trước khi sửa s."""
function lay_nhieu!(s::NganXep, k)
    if !(k isa Integer) || k isa Bool
        throw(ArgumentError("k phải là số nguyên"))
    end
    if k < 0 || k > length(s.a)
        throw(ArgumentError("k không hợp lệ"))
    end
    
    result = Int[]
    for _ in 1:k
        val = lay!(s)
        if val !== nothing
            push!(result, val)
        end
    end
    return result
end

"""Đọc k giá trị FIFO; không sửa a, dau, so, n. k sai báo ArgumentError."""
function xem_k(q::HangDoiVong, k)
    if !(k isa Integer) || k isa Bool
        throw(ArgumentError("k phải là số nguyên"))
    end
    if k < 0 || k > q.so
        throw(ArgumentError("k không hợp lệ"))
    end
    
    result = Int[]
    for i in 0:(k-1)
        push!(result, q.a[mod(q.dau + i, q.n) + 1])
    end
    return result
end

end # module
