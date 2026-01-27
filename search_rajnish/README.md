1. Linear Scan

A linear scan checks each element of the array one by one until the entire list has been processed.
It is straightforward and works on both sorted and unsorted data.

2. Binary Scan

Binary scan operates only on sorted arrays.
Instead of checking every element, it repeatedly splits the search space into halves, narrowing down where the target value can exist.

Performance Comparison

When the dataset is very small, a linear scan may appear faster because it has minimal setup and no extra computation.
However, as the size of the array grows, binary search becomes significantly more efficient.

This demonstrates why binary search is the preferred approach for large, sorted datasets, while linear scan remains suitable for small or unsorted inputs.

Benchmarking

The program compares the performance of both methods using arrays of different sizes:

10

100

1,000

10,000

100,000

For each size, it measures and displays the execution time of:

-Linear count
-Binary count

Running with Docker

Build the Docker image:

docker build -t count .


Run the container:

docker run count