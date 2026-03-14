<h2><a href="https://leetcode.com/problems/valid-anagram">242. Valid Anagram</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

### Intuition

An anagram means both strings have the exact same characters in the exact same quantities. If we count the frequency of each letter in both strings, the two frequency maps must be identical.

### Approach

1. First, verify the lengths of `s` and `t`. If they differ, they cannot be anagrams, so return `False`.
2. Use a hash map to count the occurrences of each character in the strings.
3. Python's built-in `collections.Counter` does this automatically and is highly optimized.
4. **Follow-up:** Using a hash map (like `Counter` or a standard dictionary) inherently supports Unicode characters without any modifications, unlike using a fixed-size integer array of length 26.

### Complexity

* **Time complexity:** $O(n)$
Iterating through both strings to count the characters takes linear time.
* **Space complexity:** $O(1)$
The space depends on the size of the alphabet. For lowercase English letters, the hash map stores at most 26 key-value pairs. Even for Unicode, it is bounded by the character set and does not scale infinitely with $n$.

