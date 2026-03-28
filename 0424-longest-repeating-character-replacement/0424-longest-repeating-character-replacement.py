class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0
        
        for r in range(len(s)):
            # Add the new character to our frequency map
            count[s[r]] = count.get(s[r], 0) + 1
            # Update the maximum frequency seen in the current window
            max_freq = max(max_freq, count[s[r]])
            
            # If the number of characters we need to replace exceeds k, shrink the window
            # (window length) - (most frequent character count) > k
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            # Update the max length found so far
            res = max(res, r - l + 1)
            
        return res