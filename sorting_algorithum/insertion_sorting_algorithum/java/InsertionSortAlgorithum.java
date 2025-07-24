public class InsertionSortAlgorithum {

    public static void selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int min_index = i;
            for (int j = i; j < n; j++) {

                if (arr[min_index] > arr[j]) {
                    min_index = j;
                }

            }
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    public static void main(String[] args) {
        System.out.println("Selection Sorting Algorithum");
        int[] data = { 64, 34, 25, 12, 22, 11, 90 };

        System.out.println("Array before sorting:");
        for (int num : data) {
            System.out.print(num + " ");
        }
        System.out.println();

        selectionSort(data);

        System.out.println("Array after sorting:");
        for (int num : data) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}