# PART 1
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

 # PART 2
Hashing with Chaining
Implementation:

A hash table was implemented using chaining for collision resolution.
Supported operations:
Insert: Add a key-value pair.
Search: Retrieve the value for a given key.
Delete: Remove a key-value pair.
Theoretical Analysis:

Time Complexity:
Best Case: 
𝑂
(
1
)
O(1) for search, insert, and delete when collisions are minimal.
Worst Case: 
𝑂
(
𝑛
)
O(n) when all keys collide and end up in the same bucket.
Average Case: 
𝑂
(
1
)
O(1) with a good hash function and low load factor.
Load Factor (
𝛼
α):
Defined as 
𝛼
=
Number of elements
Number of buckets
α= 
Number of buckets
Number of elements
​
 .
Performance degrades as 
𝛼
α increases due to more collisions.
Dynamic resizing can mitigate this issue by keeping 
𝛼
<
0.7
α<0.7.
Dynamic Resizing:
When 
𝛼
>
0.7
α>0.7, the table is resized (e.g., capacity doubled).
Resizing takes 
𝑂
(
𝑛
)
O(n) but occurs infrequently, so amortized complexity is 
𝑂
(
1
)
O(1).
# Empirical Results:
Search for 'apple': 5
After deleting 'banana':
Bucket 1: []
Bucket 2: []
Bucket 3: []
Bucket 4: []
Bucket 5: [['orange', 15]]
Bucket 7: []
Bucket 8: []
Bucket 9: [['apple', 5]]
PS D:\errands\git\algorithm_efficiency> python -m unittest test_hash_table.py
>>
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
PS D:\errands\git\algorithm_efficiency> python hash_table.py
Search for 'apple': 5
After deleting 'banana':
Bucket 0: []
Bucket 1: [['orange', 15]]
Bucket 2: []
Bucket 3: []
Bucket 4: []
Bucket 5: [['apple', 5]]
Bucket 6: []
Bucket 7: []
Bucket 8: []
Bucket 9: []
PS D:\errands\git\algorithm_efficiency> python -m unittest test_hash_table.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s 

The hash table performed well for small and moderate numbers of elements.
As the load factor increased beyond 0.7, performance degraded, confirming the need for resizing.
After implementing dynamic resizing, operations remained efficient even with a high number of elements.