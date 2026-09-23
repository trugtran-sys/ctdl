function insertion_sort_julia!(arr)
    for i in 2:lastindex(arr)
        key = arr[i]
        j = i - 1
        while j > 0 && arr[j] > key
            arr[j + 1] = arr[j]
            j -= 1
        end
        arr[j + 1] = key
    end
    return arr
end
A = [8, 3, 5, 1, 9, 2]
println("Julia: ", insertion_sort_julia!(A))