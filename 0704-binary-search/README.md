<h2><a href="https://leetcode.com/problems/binary-search">704. Binary Search</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt; nums[i], target &lt; 10<sup>4</sup></code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>



### Intuition
When searching for a word in a physical dictionary, you don't read every single page starting from the letter A. You open it to the middle. If the word you are looking for comes alphabetically before the page you opened, you completely ignore the entire right half of the book and repeat the process on the left half. Because the `nums` array is already sorted, we can apply this exact same logic to eliminate half of our search space with every single step.

### Approach

1. Initialize two pointers: `l` at the start (`0`) and `r` at the end (`len(nums) - 1`) of the array.
2. Enter a `while` loop that continues as long as `l` is less than or equal to `r`.
3. Calculate the middle index `mid`. Using `l + (r - l) // 2` is the universally safe way to do this to avoid integer overflow bugs that can happen with `(l + r) // 2` in languages like Java or C++.
4. Check the value at `nums[mid]`:
   * If it is exactly our `target`, we are done. Return `mid`.
   * If it is strictly greater than our `target`, the target must be in the left half. Shift the right pointer: `r = mid - 1`.
   * If it is strictly less than our `target`, the target must be in the right half. Shift the left pointer: `l = mid + 1`.
5. If the loop finishes and we haven't returned anything, the target does not exist in the array. Return `-1`.

### Complexity
* **Time complexity:** $O(\log n)$
In each step of the `while` loop, the search space is cut exactly in half. This logarithmic behavior makes binary search incredibly fast, even for massive arrays.
* **Space complexity:** $O(1)$
We only allocate a few integer variables (`l`, `r`, `mid`), which use a constant amount of memory regardless of the array's size.
