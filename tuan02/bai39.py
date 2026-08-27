import sys
import random
import time

def cach1(a):
    n = len(a)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s > max_sum:
                max_sum = s
    return max_sum
def cach2(a):
    n = len(a)
    max_sum = float('-inf')
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s > max_sum:
                max_sum = s
    return max_sum
def kadane(a):
    max_so_far = curr_max = a[0]
    for x in a[1:]:
        curr_max = max(x, curr_max + x)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
def do_thoi_gian():
    sizes = [200, 400, 800]
    for c in range(1, 4):
        times = []
        for n in sizes:
            random.seed(42)
            a = [random.randint(-100, 100) for _ in range(n)]
            runs = 5 if c == 1 else (1000 if c == 2 else 200000)
            
            t0 = time.perf_counter()
            for _ in range(runs):
                if c == 1: cach1(a)
                elif c == 2: cach2(a)
                else: kadane(a)
            t1 = time.perf_counter()
            times.append((t1 - t0) / runs)
        print(f"{times[0]:.6f} {times[1]:.6f} {times[2]:.6f}")
if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        idx = 0
        while idx < len(input_data):
            n = int(input_data[idx])
            idx += 1
            if n == 0:
                do_thoi_gian()
            else:
                a = [int(x) for x in input_data[idx:idx+n]]
                idx += n
                print(kadane(a))