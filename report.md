Time Complexity Analysis
Partitioning Time:

In each recursive call, the array is divided into two subarrays using the partitioning function.
The partition step involves iterating through the array once to place elements smaller than the pivot to its left and larger elements to its right.
Thus, the time complexity of the partitioning step is 
𝑂
(
𝑛
)
O(n), where 
𝑛
n is the number of elements in the subarray being partitioned.
Recursive Calls:

After partitioning, the algorithm recursively applies the same process to the two subarrays (left and right of the pivot).
In the average case, the pivot divides the array into two roughly equal parts. This results in a recursion tree of height 
𝑂
(
log
⁡
𝑛
)
O(logn), where 
𝑛
n is the size of the array.
At each level of the recursion tree, the partitioning work is 
𝑂
(
𝑛
)
O(n), and the total work across all levels is:
𝑇
(
𝑛
)
=
𝑛
+
𝑛
2
+
𝑛
4
+
⋯
+
1
T(n)=n+ 
2
n
​
 + 
4
n
​
 +⋯+1
Using the formula for the sum of a geometric series, this simplifies to 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
Indicator Random Variables:

The expected cost of Randomized Quicksort depends on the random choice of the pivot.
Let 
𝑋
𝑖
𝑗
X 
ij
​
  be an indicator variable that is 1 if element 
𝑖
i is compared with 
𝑗
j during the execution of the algorithm.
The probability that two elements are compared in Randomized Quicksort is at most 
2
𝑗
−
𝑖
+
1
j−i+1
2
​
 , leading to an average number of comparisons of 
≈
2
𝑛
log
⁡
𝑛
≈2nlogn.
Worst-Case Complexity:

In the worst case (e.g., when the pivot always splits the array into 
𝑛
−
1
n−1 and 1 elements), the recursion tree has height 
𝑂
(
𝑛
)
O(n), and the time complexity becomes 
𝑂
(
𝑛
2
)
O(n 
2
 ).
Summary:

Average-case time complexity: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
Worst-case time complexity: 
𝑂
(
𝑛
2
)
O(n 
2
 ), which occurs rarely due to random pivot selection.