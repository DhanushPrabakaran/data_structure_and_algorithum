arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)

print("Bubble Sorting Algorithum")
print("Array before sorting:")
print(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

print("Array after sorting:")
print(arr)