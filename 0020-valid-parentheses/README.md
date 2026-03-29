<h2><a href="https://leetcode.com/problems/valid-parentheses">20. Valid Parentheses</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()[]{}&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([])&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([)]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>

### Intuition
This is the classic use case for a **Stack** data structure (LIFO - Last In, First Out). Since valid parentheses must close in the exact reverse order that they were opened, we can push every open bracket onto a stack. The moment we encounter a closing bracket, it *must* match the bracket sitting at the very top of our stack. If it doesn't, or if the stack is empty when we try to close a bracket, the string is invalid.

### Approach

1. Initialize an empty list `stack` to keep track of open brackets.
2. Create a Hash Map `close_to_open` that maps every closing bracket to its corresponding opening bracket. This makes lookups instantly $O(1)$ and keeps the code clean.
3. Iterate through every character `c` in the string `s`:
   * **If `c` is a closing bracket** (exists in our hash map): Check if the `stack` is not empty and if the top of the `stack` (`stack[-1]`) matches the required opening bracket (`close_to_open[c]`). If it matches, `pop()` it from the stack. If it doesn't match (or stack is empty), return `False`.
   * **If `c` is an opening bracket**: Simply `append()` it to the top of the stack.
4. After checking all characters, the `stack` should be completely empty if every bracket was properly closed. Return `True` if `not stack`, else `False`.

### Complexity
* **Time complexity:** $O(n)$
We traverse the string of length $n$ exactly once. Pushing to and popping from the end of a list in Python are both $O(1)$ operations, as are dictionary lookups.
* **Space complexity:** $O(n)$
In the worst-case scenario (e.g., `"(((((("`), we will push every single character in the string onto the stack, requiring space proportional to the length of the string.
