<h2><a href="https://leetcode.com/problems/product-of-array-except-self">238. Product of Array Except Self</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>



### Intuition
Since division is forbidden, the product of the array *except* `nums[i]` is simply the product of everything to its **left** multiplied by the product of everything to its **right**. We can calculate these left (prefix) and right (postfix) products in two separate sweeps.

### Approach

1. Initialize an output array `res` of the same length as `nums`, filled with `1`s.
2. **First Pass (Prefixes):** Iterate left-to-right. For each index `i`, store the running `prefix` product in `res[i]`, then multiply the `prefix` by the current `nums[i]` for the next iteration.
3. **Second Pass (Postfixes):** Iterate right-to-left. For each index `i`, multiply the existing value in `res[i]` by the running `postfix` product. Then, multiply the `postfix` by the current `nums[i]` for the next iteration.
4. Return `res`.

### Complexity
* **Time complexity:** $O(n)$
We iterate through the array exactly twice (one forward pass, one backward pass), which takes strictly linear time.
* **Space complexity:** $O(1)$
The problem explicitly states that the output array does not count toward extra space. The only auxiliary variables we use are `prefix` and `postfix`, taking constant space.
