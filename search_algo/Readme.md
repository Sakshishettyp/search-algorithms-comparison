## Search Algorithms Benchmark

This project compares "Linear Search*" and "Binary Search" in Python for counting the number of occurrences of a value in a "sorted array". The goal is to benchmark both approaches and understand their performance differences.

## Project Contents

- 'linear_search_sol.py' – Linear scan implementation.
- 'binary_search_sol.py' – Binary search implementation.
- 'benchmark_sol.py' – Benchmarks execution time of both methods on arrays of increasing size.
- 'Dockerfile'– Run the benchmark in a container for reproducibility.
- '.gitignore' – Ignore unnecessary files.

## Usage
To run locally:
Navigate to the project folder:-
command:- cd search-algorithms-comparison/search_algo
Run the benchmark:-
 command:- python benchmark_sol.py
The benchmark prints execution times for Linear Search vs Binary Search for arrays of increasing size.

## Run with Docker

Build the Docker image:
command:-
cd search-algorithms-comparison/search_algo 
docker build -t search-benchmark .

Run the benchmark inside a container:
command:-docker run --rm search-benchmark

The container runs the benchmark without requiring Python or dependencies installed locally.

## Performance Insights

Linear Search:
Iterates through every element sequentially.
Time complexity: O(n)
Execution time grows linearly with array size.
Slower for very large arrays.

Binary Search:
Uses divide-and-conquer on sorted arrays to find first and last positions.
Time complexity: O(log n)
Execution time grows slowly even for large arrays.
Much faster on large datasets.

Conclusion: Binary Search significantly outperforms Linear Search for large sorted arrays, as demonstrated by the benchmark results.

## Sample Benchmark Output
Array Size | Linear Time (s) | Binary Time (s)
        10 |        0.00001   |      0.00001
       100 |        0.00005   |      0.00001
     1,000 |        0.00050   |      0.00001
    10,000 |        0.00500   |      0.00002
   100,000 |        0.05000   |      0.00003
 1,000,000 |        0.50000   |      0.00004
10,000,000 |        5.00000   |      0.00005

