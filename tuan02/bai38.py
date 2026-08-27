import sys

def da_sap_xep(a, nghiem_ngat=False) -> bool:
    for i in range(len(a) - 1):
        if nghiem_ngat:
            if a[i] >= a[i + 1]:
                return False
        else:
            if a[i] > a[i + 1]:
                return False
    return True
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        a = [int(x) for x in data[1:n+1]]
        nn = da_sap_xep(a, nghiem_ngat=True)
        kg = da_sap_xep(a, nghiem_ngat=False)
        res_nn = "YES" if nn else "NO"
        res_kg = "YES" if kg else "NO"
        print(f"{res_nn} - {res_kg}")