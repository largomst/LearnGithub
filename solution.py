def Solution(arr, n):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] <= n:
            new_arr.append(arr[i])

    return new_arr

print(Solution([3, 5, 6, 2, 96, 34, 32], 20))
