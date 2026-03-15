<h2><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array">448. Find All Numbers Disappeared in an Array</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>


### Intuition

Since the array elements are restricted to the range `[1, n]` and the array itself is of length `n`, we can use the input array itself as our hash map. By treating the absolute value of each number as an index, we can mark that index to indicate we've seen the number. The smartest way to "mark" it without destroying the original value is to make it negative.

### Approach

1. Iterate through the array. For every number `num` you look at, take its absolute value.
2. Calculate the index that this number maps to: `index = abs(num) - 1`.
3. Go to that `index` in the array. If the number there is positive, multiply it by `-1`. If it's already negative, leave it alone (it means we've seen this number before).
4. Do a second pass through the array.
5. Any index that still contains a positive number means we never encountered the value `index + 1` during our first pass. Collect these missing values.

### Complexity

* **Time complexity:** $O(n)$
We iterate through the array exactly twice. The mathematical operations and index lookups take $O(1)$ time per element.
* **Space complexity:** $O(1)$
We modify the input array in place. The problem description explicitly states that the returned list does not count as extra space, so our auxiliary space is constant.
