<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement">424. Longest Repeating Character Replacement</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.</p>

<p>Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ABAB&quot;, k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two &#39;A&#39;s with two &#39;B&#39;s or vice versa.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;AABABBA&quot;, k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one &#39;A&#39; in the middle with &#39;B&#39; and form &quot;AABBBBA&quot;.
The substring &quot;BBBB&quot; has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>


### Intuition
To maximize the length of a repeating character string, we want to find a window where the majority of characters are already the same, and we just use our `k` replacements to fix the few odd ones out. 

How do we mathematically know if a window is valid? We take the total length of the window and subtract the count of the most frequent character. The result is the exact number of characters we *must* change. If this number is greater than `k`, our window has too many different characters, and we must shrink it from the left.

### Approach

1. Initialize a Hash Map `count` to track the frequency of characters in your current window.
2. Use two pointers, `l` and `r`, starting at index `0`.
3. Keep a `max_freq` variable to track the highest count of a single character in the window.
4. Iterate through the string with the right pointer `r`. For each character `s[r]`, increment its count in the hash map and update `max_freq`.
5. Check if the current window is invalid. The formula is: `(r - l + 1) - max_freq > k`. 
6. If it is invalid, we slide the left side of the window forward: decrement the count of `s[l]` in the hash map, and increment `l` by 1. *(Note: We don't strictly need to downgrade `max_freq` here, because a smaller `max_freq` won't help us find a larger overall window length later).*
7. After ensuring the window is valid, update `res` with the maximum window size seen so far `(r - l + 1)`.

### Complexity
* **Time complexity:** $O(n)$
Both the left and right pointers only move forward through the string. Calculating the window size and updating the hash map takes $O(1)$ time per step.
* **Space complexity:** $O(1)$
The problem constraints state that the string only contains uppercase English letters. Therefore, the hash map `count` will never store more than 26 key-value pairs, making the auxiliary space constant.
