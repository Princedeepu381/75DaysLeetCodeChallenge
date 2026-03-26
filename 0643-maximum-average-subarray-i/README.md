<h2><a href="https://leetcode.com/problems/maximum-average-subarray-i">643. Maximum Average Subarray I</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> consisting of <code>n</code> elements, and an integer <code>k</code>.</p>

<p>Find a contiguous subarray whose <strong>length is equal to</strong> <code>k</code> that has the maximum average value and return <em>this value</em>. Any answer with a calculation error less than <code>10<sup>-5</sup></code> will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong>Output:</strong> 12.75000
<strong>Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5], k = 1
<strong>Output:</strong> 5.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


### Intuition
Since the size of the subarray $k$ is fixed, the subarray with the maximum *average* will always be the subarray with the maximum *sum*. Instead of recalculating the sum of $k$ elements from scratch for every possible window (which is slow), we can use a "Sliding Window" technique. When the window moves one step to the right, only two things happen: a new element enters the window, and an old element leaves. We just take our previous sum, add the new number, and subtract the old number.

### Approach

1. Calculate the sum of the first $k$ elements to establish your initial window. 
2. Set `max_sum` to equal this initial `curr_sum`.
3. Start a loop from index $k$ to the end of the array to slide the window forward.
4. For each step, update `curr_sum` by adding the element entering on the right (`nums[i]`) and subtracting the element falling off the left (`nums[i - k]`).
5. Update `max_sum` if the newly calculated `curr_sum` is larger.
6. Once the loop finishes, simply return `max_sum / k` to get the average.

### Complexity
* **Time complexity:** $O(n)$
We iterate through the array essentially once. The initial sum takes $O(k)$ time, and the sliding window loop takes $O(n - k)$ time. The math operations inside the loop are all $O(1)$.
* **Space complexity:** $O(1)$
We only use two integer variables (`curr_sum` and `max_sum`) regardless of how large the input array is.
