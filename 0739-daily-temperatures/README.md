<h2><a href="https://leetcode.com/problems/daily-temperatures">739. Daily Temperatures</a></h2><h3>Medium</h3><hr><p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li>
</ul>


### Intuition
This problem asks for the "Next Greater Element", which is a massive giveaway that you should use a **Monotonic Stack**. 

The goal is to keep a stack of past days that are still waiting for a warmer day. To do this efficiently, the stack strictly maintains decreasing temperatures. The moment you encounter a temperature hotter than the one sitting at the top of your stack, you know you've finally found the "warmer day" for that past day.

### Approach

1. Initialize an array `res` of the same length as `temperatures`, filled with `0`s. This automatically handles the case where a warmer day is never found.
2. Initialize an empty `stack`. Instead of storing the actual temperatures, store their **indices**. This gives you access to both the temperature value (via `temperatures[index]`) and the day it occurred (the index itself) to calculate the distance.
3. Iterate through the array using `enumerate` to get both the index `i` and the temperature `t`.
4. Check if the current temperature `t` is strictly greater than the temperature at the index stored at the top of the stack (`temperatures[stack[-1]]`).
5. If it is, pop the index from the stack. The wait time is the difference between the current day and the popped day (`i - stack_i`). Store this in `res[stack_i]`.
6. Keep popping as long as the current temperature is hotter than the top of the stack.
7. Push the current day's index `i` onto the stack.

### Complexity
* **Time complexity:** $O(n)$
You iterate through the array once. Even though there is a `while` loop inside the `for` loop, every single index is pushed onto the stack exactly once and popped exactly once. The operations inside the loop are $O(1)$, making the overall time linear.
* **Space complexity:** $O(n)$
In the worst-case scenario (the temperatures are strictly decreasing, like `[100, 90, 80, 70]`), no days will ever be resolved, and you will push every single index onto the stack.
