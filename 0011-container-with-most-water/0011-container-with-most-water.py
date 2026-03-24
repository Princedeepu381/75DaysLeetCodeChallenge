class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            # The height of the container is bottlenecked by the shorter line
            current_area = (r - l) * min(height[l], height[r])
            res = max(res, current_area)
            
            # Always move the pointer of the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res