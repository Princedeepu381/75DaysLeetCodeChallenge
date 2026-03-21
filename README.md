# LeetCode 75 Challenge - Python Solutions

This repository contains optimized Python solutions for the LeetCode 75 study plan and related algorithmic challenges. Solutions prioritize optimal time and space complexity, utilizing Python's built-in data structures (like Hash Maps and Hash Sets) and algorithmic patterns (like Two Pointers and Bucket Sort).

## 📚 Problems Solved

| # | Problem | Difficulty | Time | Space | Core Concept / Pattern |
|---|---|---|---|---|---|
| 1 | Two Sum | Easy | O(n) | O(n) | Hash Map |
| 217 | Contains Duplicate | Easy | O(n) | O(n) | Hash Set |
| 242 | Valid Anagram | Easy | O(n) | O(1) | Hash Map / Counting |
| 448 | Find All Numbers Disappeared | Easy | O(n) | O(1) | In-place Array Modification |
| 49 | Group Anagrams | Medium | O(N*K log K) | O(N*K) | Hash Map + Sorting / Tuple Keys |
| 347 | Top K Frequent Elements | Medium | O(n) | O(n) | Bucket Sort |
| 238 | Product of Array Except Self | Medium | O(n) | O(1) | Prefix/Postfix Arrays |
| 125 | Valid Palindrome | Easy | O(n) | O(1) | Two Pointers |
| 26 | Remove Duplicates from Sorted Array | Easy | O(n) | O(1) | Two Pointers |
| 283 | Move Zeroes | Easy | O(n) | O(1) | Two Pointers |

## 🚀 How to Run

Each solution is encapsulated in a `Solution` class following LeetCode's format. To test a solution locally in your Python environment, instantiate the class and call the method:

```python
# Example for Two Sum:
sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9)) 
# Output: [0, 1]
