def giai_n_hau():
  n = int(input("Nhập n: "))
  global so_nut, so_loi_giai, first_sol
  so_nut = 0
  so_loi_giai = 0
  first_sol = None
  x = [0] * (n + 1)
  cot = [True] * (n + 1)
  cheo1 = [True] * (2 * n + 1)
  cheo2 = [True] * (2 * n + 1)
  def backtrack(i):
    global so_nut, so_loi_giai, first_sol
    so_nut += 1
    if i > n:
      so_loi_giai += 1
      if first_sol is None:
        first_sol = list(x[1 : n + 1])
      return
    for j in range(1, n + 1):
      if cot[j] and cheo1[i - j + n] and cheo2[i + j - 1]:
        x[i] = j
        cot[j] = cheo1[i - j + n] = cheo2[i + j - 1] = False
        backtrack(i + 1)
        cot[j] = cheo1[i - j + n] = cheo2[i + j - 1] = True
  backtrack(1)
  print(f"Số nút đã duyệt: {so_nut}")
  print(f"Số lời giải: {so_loi_giai}")
  if first_sol:
    print(f"Bàn cờ lời giải đầu tiên (x): {first_sol}")
giai_n_hau()    