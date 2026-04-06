<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">153. Find Minimum in Rotated Sorted Array</a></h2><h3>Medium</h3><hr><p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>



### Intuition
In a normal sorted array, the numbers strictly increase. Because this array is rotated, there is exactly one "pivot" point where the sequence breaks and drops from a high number down to the absolute minimum. 

We can use Binary Search to find this drop. By comparing the middle element to the rightmost element, we instantly know which half of the array contains the pivot. If the middle number is greater than the right number, the sequence is broken on the right side, so the minimum must be over there. If the middle number is less than the right number, the right side is perfectly sorted, meaning the drop already happened on the left side (or we are currently sitting right on it).

### Approach

1. Initialize a left pointer `l` at `0` and a right pointer `r` at `len(nums) - 1`.
2. Enter a `while` loop that continues strictly while `l < r`. (We don't use `<=` because we want the pointers to converge on the exact minimum element).
3. Calculate the middle index `mid`.
4. Compare `nums[mid]` to `nums[r]`:
   * If `nums[mid] > nums[r]`, the array from `mid` to `r` is unsorted. The minimum has to be to the right of `mid`. Shift the left pointer: `l = mid + 1`.
   * If `nums[mid] <= nums[r]`, the array from `mid` to `r` is perfectly sorted. The minimum could be `nums[mid]` itself, or it could be to the left. Shift the right pointer: `r = mid`. (Notice we don't do `mid - 1` because `mid` might literally be the minimum!).
5. Once the loop terminates, `l` and `r` will point to the exact same index. Return `nums[l]`.

### Complexity
* **Time complexity:** $O(\log n)$
By discarding half of the remaining array at every step, the algorithm runs in logarithmic time, strictly satisfying the problem's $O(\log n)$ requirement.
* **Space complexity:** $O(1)$
We only allocate a few integer variables (`l`, `r`, `mid`), which use a constant amount of memory.
