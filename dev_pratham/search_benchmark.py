#Liner Search
def liner_count(arr, x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
        elif i > x:
            break
    return count


import bisect

#Binay Search
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
        liner_count(arr, size // 2)
        liner_time = time.perf_counter() - start

        start = time.perf_counter()
        binary_count(arr, size // 2)
        binary_time = time.perf_counter() - start

        print(f"Size: {size}, liner_time: {liner_time:10.10f}, binary_time: {binary_time:10.10f}")


a = [1, 1, 2, 4, 5, 5, 7, 9]
x = 5
print("Linear Count value: ",liner_count(a, x))
print("Binary Count value: ",binary_count(a, x))

benchmark()


'''
Output:
Linear Count value:  2
Binary Count value:  2
Size: 10, liner_time: 0.0000009000, binary_time: 0.0000011000
Size: 100, liner_time: 0.0000029000, binary_time: 0.0000011000
Size: 1000, liner_time: 0.0000230001, binary_time: 0.0000010999
Size: 10000, liner_time: 0.0002488000, binary_time: 0.0000017000
Size: 100000, liner_time: 0.0033508000, binary_time: 0.0000056999
Size: 1000000, liner_time: 0.1047675000, binary_time: 0.0000071999
Size: 10000000, liner_time: 1.3514788999, binary_time: 0.0000097000
'''