class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            # If the middle element is strictly greater than the rightmost element,
            # the pivot (minimum) must be somewhere to the right.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the right side is properly sorted, 
            # meaning the minimum is either at mid or to its left.
            else:
                r = mid
                
        # When l == r, we have found the minimum element
        return nums[l]