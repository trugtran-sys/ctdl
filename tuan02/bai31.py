import sys
def thong_ke(a):
    tong = sum(a)
    trung_binh = tong / len(a)
    nho_nhat = min(a)
    lon_nhat = max(a)
    return tong, trung_binh, nho_nhat, lon_nhat

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    tong, trung_binh, nho_nhat, lon_nhat = thong_ke(a)
    print(f"{tong} {trung_binh:.4f} {nho_nhat} {lon_nhat}")
if __name__ == "__main__":
    main()