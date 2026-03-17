<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">347. Top K Frequent Elements</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,2,2,3], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2,1,2,3,1,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>


### Intuition
To solve this in better than $O(n \log n)$ time, we cannot use standard sorting. However, because the maximum possible frequency of any number is bounded by the length of the array $n$, we can use a technique called Bucket Sort. By using the *frequency* of a number as the *index* in an array, we can automatically sort the elements by their counts in strictly linear $O(n)$ time.

### Approach

1. Use a hash map (like `collections.Counter`) to count the frequency of each number in the array.
2. Create an array of empty lists called `freq`. The size must be $n + 1$ because the maximum frequency a number can have is $n$ (if the array is all the same number). The *index* of this array will represent the frequency.
3. Iterate through the hash map. For each `number` and its `count`, append the `number` to the list at `freq[count]`. 
4. Create an empty `res` list.
5. Iterate backwards through the `freq` array (starting from the highest possible frequency). Whenever you find numbers at an index, append them to `res`.
6. Stop and return `res` as soon as its length reaches $k$.

### Complexity
* **Time complexity:** $O(n)$
Counting the elements takes $O(n)$ time. Populating the frequency array takes $O(n)$ time. Traversing the frequency array from right to left takes $O(n)$ time. 
* **Space complexity:** $O(n)$
The hash map stores at most $n$ unique elements. The bucket array `freq` also takes $O(n)$ space to store the $n$ elements across the sub-lists.
