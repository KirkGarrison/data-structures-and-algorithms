def binary_search(arr, x):
    low_num = 0
    high_num = len(arr) - 1
    mid_num = 0
    while low_num <= high_num:
        mid_num = (high_num + low_num) // 2
        if arr[mid_num] < x:
            low_num = mid_num + 1
        elif arr[mid_num] > x:
            high_num = mid_num - 1
        else:
            return mid_num
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
results = binary_search(arr, x)
if results != -1:
    print("Element is at index", str(results))
else:
    print("Element not found")
