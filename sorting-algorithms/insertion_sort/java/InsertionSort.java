public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("Insertion Sorting Algorithm");
        System.out.println("Array before sorting:");
        printArray(arr);
        
        insertionSort(arr);
        
        System.out.println("Array after sorting:");
        printArray(arr);
    }

    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int currentValue = arr[i];
            int insertIndex = i;

            while (insertIndex > 0 && arr[insertIndex - 1] > currentValue) {
                arr[insertIndex] = arr[insertIndex - 1];
                insertIndex--;
            }
            arr[insertIndex] = currentValue;
        }
    }

    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}