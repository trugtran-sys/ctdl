function find_pair_with_sum(arr, S)
    sort!(arr) 
    left = 1
    right = length(arr)
    while left < right
        current_sum = arr[left] + arr[right]
        if current_sum == S
            return (arr[left], arr[right])
        elseif current_sum < S
            left += 1
        else
            right -= 1
        end
    end
    return nothing
end

A = [8, 3, 5, 1, 9, 2]
S = 10
println("Julia Two Pointers Pair: ", find_pair_with_sum(A, S))