<h2><a href="https://leetcode.com/problems/move-zeroes">283. Move Zeroes</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?


### Intuition
This requires an in-place modification similar to removing duplicates. By using a two-pointer approach, we can track the boundary of our non-zero elements. Every time we encounter a non-zero number, we swap it with the first available zero (tracked by our slow pointer). This naturally pushes all non-zeroes to the front in their original order, while accumulating the zeroes at the back.

### Approach

1. Initialize a pointer `l` at index `0`. This will point to the next available position where a non-zero element should go.
2. Iterate through the array with a second pointer `r` (using a `for` loop).
3. Check the value at `nums[r]`. 
4. If it is `0`, do nothing and let `r` move forward.
5. If it is **not** `0`, swap the elements at `l` and `r`. 
6. After swapping, increment `l` by `1` to point to the next available spot. 

### Complexity
* **Time complexity:** $O(n)$
We traverse the array exactly once with the `r` pointer. The swapping operation takes $O(1)$ time.
* **Space complexity:** $O(1)$
The array is modified strictly in-place, requiring no extra memory outside of the two pointer variables.
