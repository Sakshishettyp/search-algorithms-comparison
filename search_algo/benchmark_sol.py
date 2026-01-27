import random
import time

# Import your search functions
from linear_search_sol import count_linear
from binary_search_sol import count_occurrences_binary


def benchmark():
    """
    Compare execution time of linear search vs binary search
    for counting occurrences in sorted arrays of increasing size.
    """

    # Array sizes to test
    array_sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]

    # Print a clean table header
    print("Benchmarking Linear Search vs Binary Search\n")
    print(f"{'Array Size':>12} | {'Linear Time (s)':>15} | {'Binary Time (s)':>15}")
    print("-" * 50)

    for size in array_sizes:
        # Generate a sorted array of random numbers
        numbers = sorted(random.randint(1, 100) for _ in range(size))

        # Pick a random value from the array to count
        value_to_find = random.choice(numbers)

        # Measure linear search time
        start = time.time()
        count_linear(numbers, value_to_find)
        linear_time = time.time() - start

        # Measure binary search time
        start = time.time()
        count_occurrences_binary(numbers, value_to_find)
        binary_time = time.time() - start

        # Print results for this array size
        print(f"{size:>12} | {linear_time:>15.6f} | {binary_time:>15.6f}")


if __name__ == "__main__":
    benchmark()
