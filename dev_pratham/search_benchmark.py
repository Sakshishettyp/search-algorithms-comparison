#Linear Search
def linear_count(arr, x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
        elif i > x:
            break
    return count


import bisect

#Binary Search
def binary_count(arr, x):
    first = bisect.bisect_left(arr, x)
    if first == len(arr) or arr[first] != x:
        return 0
    
    last = bisect.bisect_right(arr, x)

    return last - first

import random
import time

#Benchmark
def benchmark():
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        arr = sorted([random.randint(0, size // 2) for _ in range(size)])

        start = time.perf_counter()
        linear_count(arr, size // 2)
        linear_time = time.perf_counter() - start

        start = time.perf_counter()
        binary_count(arr, size // 2)
        binary_time = time.perf_counter() - start

        print(f"Size: {size}, linear_time: {linear_time:10.10f}, binary_time: {binary_time:10.10f}")


a = [1, 1, 2, 4, 5, 5, 7, 9]
x = 5
print("Linear Count value: ",linear_count(a, x))
print("Binary Count value: ",binary_count(a, x))

benchmark()


'''
Output:
Linear Count value:  2
Binary Count value:  2
Size: 10, linear_time: 0.0000009000, binary_time: 0.0000015000
Size: 100, linear_time: 0.0000030000, binary_time: 0.0000009000
Size: 1000, linear_time: 0.0000242001, binary_time: 0.0000008000
Size: 10000, linear_time: 0.0002309000, binary_time: 0.0000018000
Size: 100000, linear_time: 0.0028625999, binary_time: 0.0000055000
Size: 1000000, linear_time: 0.1148440000, binary_time: 0.0000077999
Size: 10000000, linear_time: 1.3171556999, binary_time: 0.0000083001
'''