<h2><a href="https://leetcode.com/problems/min-stack">155. Min Stack</a></h2><h3>Medium</h3><hr><p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>

<ul>
	<li><code>MinStack()</code> initializes the stack object.</li>
	<li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
	<li><code>void pop()</code> removes the element on the top of the stack.</li>
	<li><code>int top()</code> gets the top element of the stack.</li>
	<li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p>You must implement a solution with <code>O(1)</code> time complexity for each function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>


### Intuition
A standard stack allows you to push and pop in $O(1)$ time, but finding the minimum value normally requires scanning the entire stack, which takes $O(n)$ time. The trick to achieving $O(1)$ lookups for the minimum is to calculate and "remember" the lowest value at the exact moment every single element is added. If every element remembers what the minimum was at the time it was pushed, you never have to search for it later.

### Approach

1. Initialize two parallel arrays: `stack` to hold your actual data, and `min_stack` to act as a historical record of the minimum values.
2. **`push(val)`**: Always append `val` to your main `stack`. Before appending to `min_stack`, check what is currently at the top of it (which represents the lowest number seen so far). Push whichever is smaller: the new `val`, or the existing minimum. 
3. **`pop()`**: Because both stacks are updated simultaneously on every push, you just `pop()` from both of them at the exact same time. This keeps them perfectly synchronized. If the absolute minimum value is popped off the main stack, it is automatically popped off the `min_stack` too, revealing the *previous* minimum underneath it.
4. **`top()`**: Just return the last element in your main `stack` (`self.stack[-1]`).
5. **`getMin()`**: Because of our setup, the last element in `min_stack` (`self.min_stack[-1]`) is guaranteed to be the absolute minimum of all currently active elements.

### Complexity
* **Time complexity:** $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`). We are only ever appending to or popping from the very end of Python lists, and doing simple mathematical comparisons.
* **Space complexity:** $O(n)$
We are maintaining an additional array (`min_stack`) that scales perfectly 1:1 with the number of elements pushed into the main stack.
