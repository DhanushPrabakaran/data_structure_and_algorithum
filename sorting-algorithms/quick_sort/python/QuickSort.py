def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Quick Sort Algorithm")
    print("Array before sorting:")
    print(arr)
    sorted_arr = quick_sort(arr)
    print("Array after sorting:")
    print(sorted_arr)