def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Insertion Sort Algorithm")
    print("Array before sorting:")
    print(arr)
    sorted_arr = insertion_sort(arr)
    print("Array after sorting:")
    print(sorted_arr)