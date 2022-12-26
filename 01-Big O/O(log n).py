def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

arr = []

for i in range(10):
    arr.append(i)


print (binary_search(arr, x=12))


# O(log n) is considered to be very efficient for large inputs because it grows much slower than linear or quadratic time complexity.