import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FixedFormatter

# 1. Số liệu thực tế
n_vals = np.array([500, 1000, 2000, 4000])
time_cpp = np.array([0.00004, 0.00017, 0.00066, 0.00269])
time_python = np.array([0.00615, 0.02813, 0.12631, 0.53190])
n2_vals = n_vals**2

# 2. Khởi tạo giao diện
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(r'Bài 44 — Thời gian chạy sắp xếp chọn ($O(n^2)$) khi n tăng gấp đôi', fontsize=13)

# --- ĐỒ THỊ 1: Thang log-log ---
ax1.loglog(n_vals, time_cpp, marker='o', color='#0d3b66', label='C++ (g++ -O2)', linewidth=1.8)
ax1.loglog(n_vals, time_python, marker='o', color='#b23a1e', label='Python 3', linewidth=1.8)

# Đường tham chiếu
c_ref = time_cpp[0] / (n_vals[0]**2)
time_ref = c_ref * (n_vals**2)
ax1.loglog(n_vals, time_ref, linestyle='--', color='gray', label='đường tham chiếu hệ số góc 2', alpha=0.8)

ax1.set_title(r'Thang log-log: đường thẳng hệ số góc $2 \rightarrow O(n^2)$', fontsize=11)
ax1.set_xlabel('n (số phần tử)', fontsize=10)
ax1.set_ylabel('thời gian chạy (giây)', fontsize=10)

# Ép trục X chỉ hiện đúng 4 giá trị 500, 1000, 2000, 4000 (Xóa bỏ các nhãn thừa)
ax1.xaxis.set_major_locator(FixedLocator(n_vals))
ax1.xaxis.set_major_formatter(FixedFormatter(['500', '1000', '2000', '4000']))
ax1.xaxis.set_minor_formatter(plt.NullFormatter()) # Ẩn nhãn của các vạch phụ

# Bật lưới chính và lưới phụ nhạt cho đúng mẫu
ax1.grid(True, which="major", linestyle='-', alpha=0.3)
ax1.grid(True, which="minor", linestyle=':', alpha=0.2)
ax1.legend(fontsize=8, loc='upper left')

# --- ĐỒ THỊ 2: T theo n^2 ---
ax2.plot(n2_vals, time_cpp, marker='o', color='#0d3b66', label='C++ (g++ -O2)', linewidth=1.8)
ax2.plot(n2_vals, time_python, marker='o', color='#b23a1e', label='Python 3', linewidth=1.8)

ax2.set_title(r'T theo $n^2$: đường thẳng đi qua gốc $\rightarrow O(n^2)$', fontsize=11)
ax2.set_xlabel(r'$n^2$ (số phép so sánh tỉ lệ thuận với đại lượng này)', fontsize=10)
ax2.set_ylabel('thời gian chạy (giây)', fontsize=10)
ax2.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
ax2.grid(True, linestyle='-', alpha=0.3)
ax2.legend(fontsize=8, loc='upper left')

# 3. Xuất file ảnh
plt.tight_layout()
plt.savefig('do_thi_bai44_chuan.png', dpi=300)
plt.show()