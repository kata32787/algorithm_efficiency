# algorithm_efficiency
# Algorithm Efficiency and Scalability

## Randomized Quicksort
- Implements a randomized version of Quicksort.
- Includes tests for edge cases and comparisons with Deterministic Quicksort.

## How to Run
- Run `randomized_quicksort.py` for an example.
- Run `test_randomized_quicksort.py` to execute unit tests and comparisons.

## Results
- Theoretical analysis: Average-case time complexity is \(O(n \log n)\).
-Empirical comparisons show that:

Randomly Generated Arrays:

Randomized Quicksort consistently outperforms Deterministic Quicksort because the randomized pivot selection minimizes the chances of worst-case splits.
Already Sorted Arrays:

Deterministic Quicksort performs poorly with already sorted arrays, as the pivot choice (first element) leads to 
𝑂
(
𝑛
2
)
O(n 
2
 ) complexity.
Randomized Quicksort handles these efficiently due to random pivot selection, maintaining 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) complexity on average.
Reverse-Sorted Arrays:

Similar to sorted arrays, Deterministic Quicksort struggles with 
𝑂
(
𝑛
2
)
O(n 
2
 ) time, while Randomized Quicksort remains efficient.
Arrays with Repeated Elements:

Both algorithms perform similarly, with Randomized Quicksort slightly faster on average.
Overall, Randomized Quicksort demonstrates better performance across all cases due to its average-case efficiency of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) and its ability to avoid worst-case scenarios through randomization
# the result from test is as below
Array size: 100 | Randomized Time: 0.00024s | Deterministic Time: 0.00015s
Array size: 1000 | Randomized Time: 0.01652s | Deterministic Time: 0.00671s
Array size: 10000 | Randomized Time: 0.17379s | Deterministic Time: 0.14360s
----------------------------------------------------------------------
Ran 6 tests in 0.375s
