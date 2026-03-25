<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">121. Best Time to Buy and Sell Stock</a></h2><h3>Easy</h3><hr><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


### Intuition
This is a classic introductory Sliding Window / Two-Pointer problem. The goal is to buy low and sell high. As we scan through time (left to right), we want to keep track of the absolute lowest price we've seen. If we encounter a price lower than our current "buy" price, there is zero reason to keep the old buy price—any future sell day would yield a higher profit with the new, lower buy price. 

### Approach

1. Initialize a left pointer `l` (buy day) at index `0` and a right pointer `r` (sell day) at index `1`.
2. Initialize `max_profit` to `0`.
3. Loop through the array as long as `r` hasn't reached the end:
   * **Profitable scenario:** If the price at `l` is less than the price at `r`, we can make a profit. Calculate it and update `max_profit` if it's the highest we've seen.
   * **Unprofitable scenario:** If the price at `l` is greater than or equal to the price at `r`, we've found a new rock-bottom price. Shift our `l` pointer all the way to `r` so we can use this new low price for future comparisons.
   * Always increment `r` by 1 to check the next day.
4. Return `max_profit`.

### Complexity
* **Time complexity:** O(n)
We iterate through the array of prices exactly once using the right pointer `r`.
* **Space complexity:** O(1)
We only use two pointers and a variable to track profit, requiring no additional scaling memory.
