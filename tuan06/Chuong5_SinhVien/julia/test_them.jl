using Test
include("CauTruc.jl")
include("BaiLam.jl")
using .CauTruc
using .BaiLam

@testset "Kiem Thu Them Cua Sinh Vien" begin
    @testset "T13 Xoa het phan tu giong nhau" begin
        # T13: Xóa danh sách toàn phần tử giống nhau
        L = DSLK([7, 7, 7])
        so_luong_xoa = xoa_tat_ca!(L, 7)
        @test so_luong_xoa == 3
        @test L.n == 0
        @test L.dau === nothing
        @test gia_tri(L) == Int[]
    end

    @testset "T14 Lay nhieu voi k am" begin
        # T14: k âm báo lỗi, không đổi ngăn xếp
        s = NganXep()
        for x in [10, 20, 30]
            day!(s, x)
        end
        
        @test_throws ArgumentError lay_nhieu!(s, -1)
        
        @test s.a == [10, 20, 30]
    end
end
