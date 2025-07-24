function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let currentValue = arr[i];
        let insertIndex = i;

        for (let j = i - 1; j >= 0; j--) {
            if (arr[j] > currentValue) {
                insertIndex = j;
            }
        }

        arr.splice(i, 1);
        arr.splice(insertIndex, 0, currentValue);
    }
    return arr;
}

// Example usage:
const array = [64, 34, 25, 12, 22, 11, 90];
console.log("Array before sorting:", array);
console.log("Array after sorting:", insertionSort(array));