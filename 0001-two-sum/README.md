<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

### Intuition

Instead of using a nested loop to check every possible pair, we can use a hash map to keep track of the numbers we've seen and their indices. This allows us to instantly check if the exact number we need (the complement) has already appeared.

### Approach

1. Initialize an empty dictionary called `num_map`.
2. Iterate through the array `nums`, tracking both the index `i` and the value `num`.
3. Calculate the `complement` required to reach the target (`target - num`).
4. If the `complement` is already a key in `num_map`, you have found your pair. Return `[num_map[complement], i]`.
5. If it is not in the map, add the current `num` as a key with its index `i` as the value, and continue.

### Complexity

* **Time complexity:** $O(n)$
We traverse the list containing $n$ elements exactly once. Each lookup and insertion in the hash map takes $O(1)$ time on average.
* **Space complexity:** $O(n)$
The extra space required depends on the number of items stored in the hash map, which in the worst-case scenario will store $n$ elements.
