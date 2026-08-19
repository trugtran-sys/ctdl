import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    print(f"{sum(a)} {max(a)}")
if __name__ == '__main__':
    main()