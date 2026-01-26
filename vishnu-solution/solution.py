import random, time, bisect, sys

# Linear scan to count occurrences
def count_linear(a, x):
    count = 0
    for value in a:
        if value == x:
            count += 1
        elif value > x:  
            break
    return count

# Binary search using bisect to count occurrences
def count_binary(a, x):
    left = bisect.bisect_left(a, x)
    right = bisect.bisect_right(a, x)
    return right - left

def benchmark():
    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

    print(f"{'Size':>12} | {'Linear (s)':>12} | {'Binary (s)':>12}")
    print("-" * 42)

    for n in sizes:
        # Create a sorted array with duplicates
        a = sorted(random.randint(0, 100) for _ in range(n))
        x = random.choice(a) 

        # Linear scan timing
        start = time.perf_counter()
        count_linear(a, x)
        linear_time = time.perf_counter() - start

        # Binary search timing
        start = time.perf_counter()
        count_binary(a, x)
        binary_time = time.perf_counter() - start

        print(f"{n:12} | {linear_time:12.6f} | {binary_time:12.6f}")
        sys.stdout.flush()      

if __name__ == "__main__":
    benchmark()


