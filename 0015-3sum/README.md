<h2><a href="https://leetcode.com/problems/3sum">15. 3Sum</a></h2><h3>Medium</h3><hr><p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


### Intuition
If we fix one number in the array, the problem instantly breaks down into the exact same **Two Sum II** problem you already solved. By sorting the array first, we unlock the ability to use the Two-Pointer technique to find the matching pairs. Sorting also neatly groups identical numbers together, making it effortless to skip duplicates and guarantee our output only has unique triplets.

### Approach

1. **Sort the array:** This is the most crucial step. It allows two pointers and easy duplicate management.
2. **Iterate with a fixed pointer (`i`):** Loop through the array. The current number `a` acts as our first number in the triplet. 
   * *Optimization:* If `a > 0`, we can stop immediately. Because the array is sorted, all numbers to the right are also positive, meaning they can never sum to `0`.
   * *Duplicate Check:* If `a` is the same as the previous number, skip it to avoid duplicate triplets.
3. **Two Pointers (`l` and `r`):** Set the left pointer just after `i` (`l = i + 1`) and the right pointer at the end of the array.
4. **Check the Sum:** * If the sum is too big, decrement `r` to get a smaller number.
   * If the sum is too small, increment `l` to get a bigger number.
   * If the sum is exactly `0`, we found a valid triplet! Add it to the result list, and squeeze both pointers inward.
5. **Skip Inner Duplicates:** After finding a valid triplet, keep shifting the `l` pointer to the right as long as it points to the same number it just processed.

### Complexity
* **Time complexity:** $O(n^2)$
Sorting the array takes $O(n \log n)$. The outer loop runs $n$ times, and inside it, the two pointers scan the remaining part of the array, which takes $O(n)$ time. Therefore, the overall time complexity is bounded by $O(n^2)$.
* **Space complexity:** $O(1)$ or $O(n)$
Depending on the specific sorting algorithm implementation (Python's built-in `sort()` uses Timsort, which takes $O(n)$ memory in the worst case). If we ignore the memory used by the sorting algorithm and the output array, the auxiliary space is $O(1)$.
