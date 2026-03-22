<h2><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted">167. Two Sum II - Input Array Is Sorted</a></h2><h3>Medium</h3><hr><p>Given a <strong>1-indexed</strong> array of integers <code>numbers</code> that is already <strong><em>sorted in non-decreasing order</em></strong>, find two numbers such that they add up to a specific <code>target</code> number. Let these two numbers be <code>numbers[index<sub>1</sub>]</code> and <code>numbers[index<sub>2</sub>]</code> where <code>1 &lt;= index<sub>1</sub> &lt; index<sub>2</sub> &lt;= numbers.length</code>.</p>

<p>Return<em> the indices of the two numbers&nbsp;</em><code>index<sub>1</sub></code><em> and </em><code>index<sub>2</sub></code><em>, <strong>each incremented by one,</strong> as an integer array </em><code>[index<sub>1</sub>, index<sub>2</sub>]</code><em> of length 2.</em></p>

<p>The tests are generated such that there is <strong>exactly one solution</strong>. You <strong>may not</strong> use the same element twice.</p>

<p>Your solution must use only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numbers = [<u>2</u>,<u>7</u>,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numbers = [<u>2</u>,3,<u>4</u>], target = 6
<strong>Output:</strong> [1,3]
<strong>Explanation:</strong> The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numbers = [<u>-1</u>,<u>0</u>], target = -1
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
	<li><code>numbers</code> is sorted in <strong>non-decreasing order</strong>.</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
	<li>The tests are generated such that there is <strong>exactly one solution</strong>.</li>
</ul>

### Intuition
Because the array is already sorted, we do not need the $O(n)$ space of a hash map to find the complement. We can use the sorted property to our advantage by placing pointers at the smallest and largest numbers. If their sum is too big, we need a smaller number, so we shift the right pointer left. If the sum is too small, we need a bigger number, so we shift the left pointer right.

### Approach

1. Initialize a left pointer `l` at index `0` and a right pointer `r` at `len(numbers) - 1`.
2. Enter a loop that runs as long as `l < r`.
3. Calculate the sum of the elements at the two pointers: `curr_sum = numbers[l] + numbers[r]`.
4. If `curr_sum` is greater than the `target`, decrement `r` by 1.
5. If `curr_sum` is less than the `target`, increment `l` by 1.
6. If they are equal, you've found the pair. Return their 1-based indices `[l + 1, r + 1]`.

### Complexity
* **Time complexity:** $O(n)$
In the worst-case scenario, the pointers will meet in the middle, meaning we traverse the array exactly once.
* **Space complexity:** $O(1)$
We only use two integer variables (`l` and `r`) for pointers, strictly adhering to the constant extra space requirement.
