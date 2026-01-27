public class BinarySearchCount {

    public static int countOccurrences(int[] arr, int x) {
        int firstX = lowerBound(arr, x);
        int firstNext = lowerBound(arr, x+1);

        return firstNext - firstX;
    }

    private static int lowerBound(int[] arr, int target) {
        int low = 0, high = arr.length;

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}
