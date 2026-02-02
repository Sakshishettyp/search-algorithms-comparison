import random 
import time


# -------- Linear Count (Optimized) --------
def linear_count(a, x):
    count = 0
    for v in a:
        if v == x:
            count += 1
    return count


# -------- Binary Count (Optimized) --------
def binary_count(a, x):
    n = len(a)

    # Find leftmost occurrence
    start, end = 0, n - 1
    left = -1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            left = mid
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    if left == -1:
        return 0

    # Find rightmost occurrence
    start, end = left, n - 1  # optimization: start from left
    right = left
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            right = mid
            start = mid + 1
        else:
            end = mid - 1

    return right - left + 1


# -------- Test --------
a = [1, 1, 2, 4, 5, 5, 5, 7, 9]
x = 5

print("Linear count:", linear_count(a, x))
print("Binary count:", binary_count(a, x))

def bm():
    for n in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
        a = sorted(random.randint(1, 50) for i in range(n))
        x = random.randint(1, 50)

        start = time.time()
        linear_count(a, x)
        t1 = time.time() - start

        start = time.time()
        binary_count(a, x)
        t2 = time.time() - start

        print("n =", n, "linear =", t1 * 1000, "ms", "binary =", t2 * 1000, "ms")


bm()
