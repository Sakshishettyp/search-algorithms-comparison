import java.util.Random;

public class Benchmark {

    public static void main(String[] args) {

        System.out.println("Linear Search Result: " + LinearCount.countOccurrences(new int[]{1, 1, 2, 4, 5, 5, 7, 9}, 5));
        System.out.println("Binary Search Result: " + BinarySearchCount.countOccurrences(new int[]{1, 1, 2, 4, 5, 5, 7, 9}, 5));

        System.out.println("-----------------------------------");
        System.out.println("-----------------------------------");

        int[] sizes = {10, 100, 1_000, 10_000, 100_000, 1_000_000};
        Random random = new Random();

        for (int size : sizes) {
            int[] arr = random.ints(size, 1, 10)
                    .sorted()
                    .toArray();

            int x = 5;

            long startLinear = System.nanoTime();
            LinearCount.countOccurrences(arr, x);
            long endLinear = System.nanoTime();

            long startBinary = System.nanoTime();
            BinarySearchCount.countOccurrences(arr, x);
            long endBinary = System.nanoTime();

            System.out.println("Array Size: " + size);
            System.out.println("Linear Scan Time (ms): " +
                    (endLinear - startLinear) / 1_000_000.0);
            System.out.println("Binary Search Time (ms): " +
                    (endBinary - startBinary) / 1_000_000.0);
            System.out.println("-----------------------------------");
        }
    }
}
