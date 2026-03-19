class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. The Pythonic Shortcut (O(n) space, but extremely fast due to C-optimized slicing)
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]