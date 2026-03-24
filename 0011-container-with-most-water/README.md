<h2><a href="https://leetcode.com/problems/container-with-most-water">11. Container With Most Water</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

### Intuition
The area of a container is determined by `width * height`. The width is maximized when our pointers are at opposite ends of the array. Because the water level cannot be slanted, the maximum height of the water is completely limited by the *shorter* of the two lines. 

If we move the taller line inward, the width decreases, and the bottleneck height still cannot exceed the original shorter line—meaning the area will *always* decrease or stay the same. The only way to potentially find a larger area is to abandon the shorter line and move its pointer inward, hoping to find a taller line to compensate for the lost width.

### Approach

1. Initialize two pointers: `l` at the beginning (`0`) and `r` at the end (`len(height) - 1`).
2. Keep a variable `res` to track the maximum area seen so far.
3. While `l < r`:
   * Calculate the current area: multiply the distance between the pointers `(r - l)` by the minimum of the two heights `min(height[l], height[r])`.
   * Update `res` if the current area is larger.
   * Compare `height[l]` and `height[r]`. Increment `l` if the left line is shorter; otherwise, decrement `r`.
4. Return the maximum area `res` once the pointers meet.

### Complexity
* **Time complexity:** $O(n)$
We traverse the array exactly once. The two pointers move inward and meet in the middle, evaluating each line at most one time.
* **Space complexity:** $O(1)$
We only use a few integer variables (`l`, `r`, `res`, `current_area`) regardless of the size of the input array, adhering to constant extra space.

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>
