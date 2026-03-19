<h2><a href="https://leetcode.com/problems/valid-palindrome">125. Valid Palindrome</a></h2><h3>Easy</h3><hr><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>


### Intuition
A palindrome reads the same forwards and backwards. This means the first character must match the last, the second must match the second-to-last, and so on. Instead of creating a whole new cleaned string (which takes extra memory), we can just point to the start and end of the original string and walk inwards, ignoring any spaces or punctuation along the way.

### Approach

1. Initialize two pointers: `l` at the beginning of the string (index `0`) and `r` at the end (index `len(s) - 1`).
2. Loop while `l` is less than `r`.
3. If the character at `l` is not alphanumeric (a letter or number), move `l` to the right (`l += 1`) and continue.
4. If the character at `r` is not alphanumeric, move `r` to the left (`r -= 1`) and continue.
5. Once both pointers are on valid alphanumeric characters, compare their lowercase versions. 
6. If they are different, the string is not a palindrome. Return `False`.
7. If they are the same, move both pointers inward (`l += 1`, `r -= 1`) and repeat.
8. If the pointers meet or cross without finding any mismatches, return `True`.
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>
