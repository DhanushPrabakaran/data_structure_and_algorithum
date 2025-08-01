def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Array before sorting:", arr)
    selection_sort(arr)
    print("Array after sorting:", arr)