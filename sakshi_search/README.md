1. Linear Scan
Iterates through the array element by element.

2. Binary Scan
This finds an element in a sorted array by repeatedly dividing the search range in half.

For very small inputs, linear scan can sometimes be slightly faster due to lower overhead, but as the input size increases, binary search clearly performs better.
This shows why binary search is more suitable for large sorted datasets.

Benchmarking
The program benchmarks both approaches for array sizes:
10, 100, 1000, 10000, 100000

It prints the execution time for:
Linear count
Binary count

How to run with Docker

Build the image:
docker build -t count .

Run the container:
docker run count