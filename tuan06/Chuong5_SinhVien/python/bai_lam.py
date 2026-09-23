"""Hoàn thành bốn hàm. Giữ nguyên tên, tham số và quy ước trả về."""
from cau_truc import DSLK, NganXep, HangDoiVong, so_nguyen
BAN = "Sinh viên"


def dem_gia_tri(L: DSLK, x: int) -> int:
    """Đếm nút có gt == x; duyệt bằng ke, không thay đổi L."""
    count = 0
    p = L.dau
    while p is not None:
        if p.gt == x:
            count += 1
        p = p.ke
    return count


def xoa_tat_ca(L: DSLK, x: int) -> int:
    """Xoá mọi nút có gt == x; trả số nút xoá, cập nhật n đúng."""
    count = 0
    truoc = None
    p = L.dau
    while p is not None:
        if p.gt == x:
            if truoc is None:
                L.dau = p.ke
            else:
                truoc.ke = p.ke
            p = p.ke
            count += 1
            L.n -= 1
        else:
            truoc = p
            p = p.ke
    return count


def lay_nhieu(s: NganXep, k: int) -> list[int]:
    """Lấy đúng k giá trị theo LIFO; k sai thì báo ValueError trước khi sửa s."""
    if type(k) is not int or isinstance(k, bool):
        raise ValueError("k phải là số nguyên")
    if k < 0 or k > len(s.a):
        raise ValueError("k không hợp lệ")
    
    result = []
    for _ in range(k):
        val = s.lay()
        if val is not None:
            result.append(val)
    return result


def xem_k(q: HangDoiVong, k: int) -> list[int]:
    """Đọc k phần tử đầu FIFO; không sửa a, dau, so, n; k sai báo ValueError."""
    if type(k) is not int or isinstance(k, bool):
        raise ValueError("k phải là số nguyên")
    if k < 0 or k > q.so:
        raise ValueError("k không hợp lệ")
    
    result = []
    for i in range(k):
        result.append(q.a[(q.dau + i) % q.n])
    return result
