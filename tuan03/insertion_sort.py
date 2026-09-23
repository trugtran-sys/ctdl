def insertion_sort_python(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
A = [8, 3, 5, 1, 9, 2]
print("Python:", insertion_sort_python(A))