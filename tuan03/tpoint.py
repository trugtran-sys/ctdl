def find_pair_with_sum(arr, S):
    arr.sort()  
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == S:
            return (arr[left], arr[right])
        elif current_sum < S:
            left += 1
        else:
            right -= 1
    return None

A = [8, 3, 5, 1, 9, 2]
S = 10
print("Python Two Pointers Pair:", find_pair_with_sum(A, S))