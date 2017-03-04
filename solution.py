def Solution(arr, n):
    j = 0
    for i in range(len(arr)):
        if arr[i] == n:
            continue
        arr[j] = arr[i]
        j += 1
    return len(arr)

print(Solution([3, 5, 6, 2, 96, 34, 32], 20))

# Given an array and a value, remove all instances of that value in place
# and return the new length.

# Do not allocate extra space for another array, you must do this in place
# with constant memory.

# The order of elements can be changed. It doesn't matter what you leave
# beyond the new length.

# 楼主的题目居然都给错了，妈蛋

# typo type