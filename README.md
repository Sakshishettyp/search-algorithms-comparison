\# Search Algorithms Comparison



This repository compares different approaches for counting occurrences of a

value `x` in a \*\*sorted array\*\*, implemented in multiple programming languages.



The focus is on \*\*algorithmic performance and complexity\*\*, not on

language-specific optimizations.



---



\## Problem Statement



Given:

\- A sorted array `a`

\- A target value `x`



Count how many times `x` appears in the array.



\### Example


a = \[1, 1, 2, 4, 5, 5, 7, 9]

x = 5

Output: 2





---



\## Algorithms Used (Language Independent)



\### Linear Scan

\- Traverse the array sequentially

\- Count matching elements

\- Stop early when the current value exceeds `x`

\- \*\*Time Complexity:\*\* O(n)



\### Binary Search

\- Use binary search to find the first and last occurrence of `x`

\- Number of occurrences = `right\_index - left\_index`

\- \*\*Time Complexity:\*\* O(log n)



---



\## Benchmarking Approach



\- Arrays of increasing sizes are generated and sorted

\- Each algorithm is executed multiple times

\- Total execution time is measured

\- Repetition is used because single executions are too fast to measure reliably



Absolute timings may vary by language, runtime, and machine, but \*\*performance

growth trends remain consistent\*\*.



---



\## Available Implementations



\- \*\*Python\*\*: `solution.py`

\- \*\*Java\*\*: `java/SearchAlgorithmsComparison.java`



Each implementation follows the same algorithmic logic so that comparisons

remain meaningful across languages.



---



\## Running the Java Implementation



\### Run Locally

```bash

javac java/SearchAlgorithmsComparison.java

java -cp java SearchAlgorithmsComparison



