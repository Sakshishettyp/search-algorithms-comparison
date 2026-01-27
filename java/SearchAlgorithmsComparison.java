import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class SearchAlgorithmsComparison {

    // Linear scan to count occurrences
    public static int countLinear(int[] a, int x) {
        int count = 0;
        for (int value : a) {
            if (value == x) {
                count++;
            } else if (value > x) {
                break;
            }
        }
        return count;
    }

    // Binary search to count occurrences
    public static int countBinary(int[] a, int x) {
        int left = lowerBound(a, x);
        int right = upperBound(a, x);
        return right - left;
    }

    private static int lowerBound(int[] a, int x) {
        int low = 0, high = a.length;
        while (low < high) {
            int mid = (low + high) / 2;
            if (a[mid] < x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    private static int upperBound(int[] a, int x) {
        int low = 0, high = a.length;
        while (low < high) {
            int mid = (low + high) / 2;
            if (a[mid] <= x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

   public static void benchmark() {

    int[] sizes = {10, 100, 1000, 10000, 100000, 1000000};
    int repetitions = 1_000_000; // run each search many times

    for (int n : sizes) {

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = ThreadLocalRandom.current().nextInt(0, 100);
        }
        Arrays.sort(a);

        int x = a[ThreadLocalRandom.current().nextInt(n)];

        System.out.println("Array size: " + n);

        long start = System.nanoTime();
        for (int i = 0; i < repetitions; i++) {
            countLinear(a, x);
        }
        double linearTime = (System.nanoTime() - start) / 1_000_000_000.0;
        System.out.println("Linear search total time: " + linearTime + " seconds");

        start = System.nanoTime();
        for (int i = 0; i < repetitions; i++) {
            countBinary(a, x);
        }
        double binaryTime = (System.nanoTime() - start) / 1_000_000_000.0;
        System.out.println("Binary search total time: " + binaryTime + " seconds");

        System.out.println("-----------------------------------");

        // Pause so humans can see it
        try {
            Thread.sleep(1000); // 1 second pause
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}


    public static void main(String[] args) {
        benchmark();
    }
}
 