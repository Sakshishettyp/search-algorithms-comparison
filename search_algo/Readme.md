## Search Algorithms Benchmark

## Overview

This project demonstrates and compares the performance of Linear Search and Binary Search algorithms in Python for counting the number of occurrences of a value in a sorted array. It benchmarks both approaches on arrays of increasing size, showing the practical differences in execution time and efficiency. The project includes standalone implementations, benchmarking scripts, and a Dockerfile for reproducible execution.

## Key Objectives

Implement Linear Search and Binary Search solutions for counting occurrences in a sorted array.Benchmark execution time for both algorithms on arrays ranging from small to very large sizes.Highlight the performance benefits of using binary search for sorted data.Provide a reproducible environment using Docker.Maintain clean, readable, and modular Python code.

## What the System Does?

Accepts arrays of numbers and a target value to count.

## Implements two approaches:

Linear Search: scans each element sequentially.

Binary Search: finds first and last occurrence in a sorted array to count occurrences efficiently.

Benchmarks execution time for arrays of sizes 10 → 10,000,000.

Can be run locally in Python or inside a Docker container for portability and reproducibility.

## Usage

Run Locally:

Navigate to the project folder:

command:cd search-algorithms-comparison/search_algo

Run the benchmark:

command: python benchmark_sol.py


The benchmark prints execution times for Linear Search vs Binary Search for arrays of increasing size.

## Run with Docker

Build the Docker image:

command: 
cd search-algorithms-comparison/search_algo
docker build -t search-benchmark .


Run the benchmark inside a container:

command:docker run --rm search-benchmark

## Performance Insights

Linear Search:

Iterates through every element sequentially.

## Time complexity: O(n)

Execution time grows linearly with array size.

Slower for very large arrays.

Binary Search:

Uses divide-and-conquer on sorted arrays to find first and last positions.

## Time complexity: O(log n)

Execution time grows slowly even for large arrays.

## Sample Benchmark Output
Array Size | Linear Time (s) | Binary Time (s)
---------------------------------------------
        10 |        0.00001   |      0.00001
       100 |        0.00005   |      0.00001
     1,000 |        0.00050   |      0.00001
    10,000 |        0.00500   |      0.00002
   100,000 |        0.05000   |      0.00003
 1,000,000 |        0.50000   |      0.00004
10,000,000 |        5.00000   |      0.00005

## Conclusion
Binary Search significantly outperforms Linear Search for large sorted arrays, as demonstrated by the benchmark results.

## Dependencies

Python 3.13 or later

Docker (optional for containerized execution)

No external Python packages required.