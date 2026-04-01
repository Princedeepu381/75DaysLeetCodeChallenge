<h2><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation">150. Evaluate Reverse Polish Notation</a></h2><h3>Medium</h3><hr><p>You are given an array of strings <code>tokens</code> that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.</p>

<p>Evaluate the expression. Return <em>an integer that represents the value of the expression</em>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The valid operators are <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, <code>&#39;*&#39;</code>, and <code>&#39;/&#39;</code>.</li>
	<li>Each operand may be an integer or another expression.</li>
	<li>The division between two integers always <strong>truncates toward zero</strong>.</li>
	<li>There will not be any division by zero.</li>
	<li>The input represents a valid arithmetic expression in a reverse polish notation.</li>
	<li>The answer and all the intermediate calculations can be represented in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;2&quot;,&quot;1&quot;,&quot;+&quot;,&quot;3&quot;,&quot;*&quot;]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;4&quot;,&quot;13&quot;,&quot;5&quot;,&quot;/&quot;,&quot;+&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;10&quot;,&quot;6&quot;,&quot;9&quot;,&quot;3&quot;,&quot;+&quot;,&quot;-11&quot;,&quot;*&quot;,&quot;/&quot;,&quot;*&quot;,&quot;17&quot;,&quot;+&quot;,&quot;5&quot;,&quot;+&quot;]
<strong>Output:</strong> 22
<strong>Explanation:</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tokens.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tokens[i]</code> is either an operator: <code>&quot;+&quot;</code>, <code>&quot;-&quot;</code>, <code>&quot;*&quot;</code>, or <code>&quot;/&quot;</code>, or an integer in the range <code>[-200, 200]</code>.</li>
</ul>


### Intuition
Reverse Polish Notation (RPN), also known as postfix notation, is practically designed to be solved using a Stack. Because the operators always follow their operands, you can continuously push numbers onto a stack as you read them. The moment you hit an operator, you know exactly which numbers it applies to: the two most recent numbers you just looked at (which are sitting right at the top of your stack).

### Approach

1. Initialize an empty `stack` to keep track of the numbers.
2. Iterate through each `token` in the input array.
3. **If the token is a number:** Convert it to an integer and `push` it onto the stack.
4. **If the token is an operator (`+`, `-`, `*`, `/`):** * `pop` the top two numbers from the stack. *Important:* The first number popped is the right operand, and the second number popped is the left operand (e.g., for `b - a`, `a` is popped first).
   * Evaluate the mathematical expression.
   * *Python-specific gotcha:* For division, use `int(b / a)` instead of `b // a`. The problem strictly requires division to truncate toward zero (e.g., `int(6 / -132) = 0`), whereas Python's `//` operator truncates toward negative infinity (`6 // -132 = -1`).
   * `push` the calculated result back onto the stack.
5. Once the loop finishes, the entire expression will have collapsed into a single number. Return `stack[0]`.

### Complexity
* **Time complexity:** $O(n)$
We iterate through the array of `n` tokens exactly once. Pushing to and popping from a stack, as well as basic arithmetic operations, all take $O(1)$ time.
* **Space complexity:** $O(n)$
In the worst-case scenario (an expression with many numbers and only a few operators at the very end), the stack will store up to $(n + 1) / 2$ numbers, which simplifies to a linear space requirement.
