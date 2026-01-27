## Counting Occurrences in a Sorted Array

This solution compares two approaches to count the occurrences of a value `x` in a sorted array.

### Approaches
1. Linear scan – O(n)
2. Binary search – O(log n)

### Benchmarking
Benchmarks were run on randomly generated sorted arrays of sizes:
10, 100, 1,000, ..., 1,000,000.

### Observations
- Linear scan time grows linearly with array size.
- Binary search remains nearly constant even for very large arrays.
- For large inputs, binary search performs significantly better.

### Conclusion
Binary search is the preferred approach when working with sorted arrays,
especially for large input sizes.

## Run Using Docker

```bash
docker build -t count-occurrences-java .
docker run --rm count-occurrences-java
```