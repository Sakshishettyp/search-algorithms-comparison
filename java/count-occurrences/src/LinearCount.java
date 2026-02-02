public class LinearCount {

    public static int countOccurrences(int[] arr, int x) {
        int count = 0;
        for (int value : arr) {
            if (value == x) {
                count++;
            }
        }
        return count;
    }
}
