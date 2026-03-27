<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">3. Longest Substring Without Repeating Characters</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3. Note that <code>&quot;bca&quot;</code> and <code>&quot;cab&quot;</code> are also correct answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>



### Intuition
We can solve this efficiently using a dynamic "Sliding Window." As we read through the string, we expand our window to the right. To guarantee the substring has no duplicates, we can use a Hash Set to track the characters currently inside our window. The moment we encounter a character that is already in our set, our window becomes invalid. To fix it, we simply shrink the window from the left side, removing characters from the set one by one, until the duplicate is gone. 

### Approach

1. Initialize a Hash Set `char_set` to store the characters in the current window.
2. Initialize a left pointer `l` at `0` and a `max_len` variable to track the longest valid substring seen.
3. Use a `for` loop to iterate through the string with a right pointer `r`.
4. Inside the loop, check if `s[r]` is already in `char_set`.
5. If it is, we have a duplicate. Use a `while` loop to remove `s[l]` from the set and increment `l` forward until `s[r]` is no longer in the set.
6. Add the current character `s[r]` to the set.
7. Calculate the current window's size (`r - l + 1`) and update `max_len` if this size is the largest we've encountered.

### Complexity
* **Time complexity:** $O(n)$
In the worst-case scenario (e.g., "abccba"), both the `l` and `r` pointers will traverse the entire string exactly once. Adding to and removing from a Python set takes $O(1)$ time on average. 
* **Space complexity:** $O(m)$
The space is dictated by the size of the set, where $m$ is the maximum number of unique characters in the string. Since the problem mentions English letters, digits, and symbols, the character set is essentially bounded by the ASCII character limit (typically 128 or 256), making the space complexity effectively $O(1)$ constant memory overhead.
