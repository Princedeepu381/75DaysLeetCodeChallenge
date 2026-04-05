<h2><a href="https://leetcode.com/problems/search-a-2d-matrix">74. Search a 2D Matrix</a></h2><h3>Medium</h3><hr><p>You are given an <code>m x n</code> integer matrix <code>matrix</code> with the following two properties:</p>

<ul>
	<li>Each row is sorted in non-decreasing order.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p>Given an integer <code>target</code>, return <code>true</code> <em>if</em> <code>target</code> <em>is in</em> <code>matrix</code> <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>You must write a solution in <code>O(log(m * n))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-10<sup>4</sup> &lt;= matrix[i][j], target &lt;= 10<sup>4</sup></code></li>
</ul>

### Intuition
Because every row is strictly sorted and the start of each row is greater than the end of the previous one, this 2D matrix is completely perfectly sorted. If you were to flatten the matrix out, it would just be one long, standard 1D sorted array. 

Instead of actually wasting time and memory flattening it, we can just *pretend* it's a 1D array. We can run a normal Binary Search from `0` to `total_elements - 1`, and just use a bit of math to translate our 1D `mid` pointer back into the real 2D `(row, col)` coordinates.

### Approach

1. Define the boundaries of your imaginary 1D array: `l = 0` and `r = ROWS * COLS - 1`.
2. Start the standard Binary Search `while l <= r`.
3. Find the `mid` index.
4. **The Magic Formula:** Convert `mid` into a 2D coordinate. 
   * `row = mid // COLS` (Floor division tells you how many full rows fit into `mid`).
   * `col = mid % COLS` (Modulo tells you the leftover remainder, which is the column index).
5. Compare the `target` to `matrix[row][col]`.
   * If the matrix value is too big, move `r = mid - 1`.
   * If the matrix value is too small, move `l = mid + 1`.
   * If it matches, return `True`.
6. Return `False` if the loop finishes without finding the target.

### Complexity
* **Time complexity:** $O(\log(m \times n))$
Since we treat the entire matrix of $m$ rows and $n$ columns as a single array of size $m \times n$, the binary search divides the search space in half each time. This satisfies the strict time complexity requirement of the problem.
* **Space complexity:** $O(1)$
We only use a few integer variables for our pointers and calculations, requiring no extra memory.
