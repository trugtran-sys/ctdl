import unittest
from cau_truc import DSLK, NganXep
from bai_lam import xoa_tat_ca, lay_nhieu

class TestSinhVienThem(unittest.TestCase):
    def test_t13_xoa_het_phan_tu_giong_nhau(self):
        # T13: Xóa danh sách toàn phần tử giống nhau (Kiểm tra biên)
        L = DSLK([7, 7, 7])
        so_luong_xoa = xoa_tat_ca(L, 7)
        self.assertEqual(so_luong_xoa, 3)
        self.assertEqual(L.n, 0)
        self.assertIsNone(L.dau)
        self.assertEqual(L.gia_tri(), [])
        
    def test_t14_lay_nhieu_k_am(self):
        # T14: k âm báo lỗi, không đổi ngăn xếp (Kiểm tra ngoại lệ)
        s = NganXep()
        for x in [10, 20, 30]:
            s.day(x)
            
        with self.assertRaises(ValueError):
            lay_nhieu(s, -1)
            
        # Đảm bảo ngăn xếp không bị mất dữ liệu
        self.assertEqual(s.a, [10, 20, 30])

if __name__ == '__main__':
    unittest.main(verbosity=2)
