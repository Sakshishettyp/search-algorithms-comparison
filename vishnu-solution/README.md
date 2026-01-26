# Search Algorithms Comparison

Benchmarks linear vs binary search for counting occurrences in sorted arrays.

## What We're Doing

This solution compares the performance of two search algorithms for counting how many times a value appears in a sorted array:

### Linear Search

- **How it works**: Iterates through the array sequentially from start to end, counting matches
- **Optimization**: Stops when encountering a value greater than the target (since array is sorted)

### Binary Search

- **How it works**: Uses `bisect_left` and `bisect_right` to find the leftmost and rightmost positions of the target value
- **Advantage**: Much faster on large datasets by dividing the search space in half repeatedly

## Run with Docker

```bash
docker build -t search-algo .
docker run search-algo
```

## Run Locally

```bash
python solution.py
```

## Output

Displays performance comparison across array sizes from 10 to 1,000,000 elements, showing how binary search significantly outperforms linear search as data grows.
