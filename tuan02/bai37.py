import sys

def dem(a):
    chan = sum(1 for x in a if x % 2 == 0)
    le = sum(1 for x in a if x % 2 != 0)
    am = sum(1 for x in a if x < 0)
    return (chan, le, am)
if __name__ == '__main__':
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        a = [int(x) for x in data[1:n+1]]
        chan, le, am = dem(a)
        print(f"chan {chan}, le {le}, am {am}")