class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if the left half is perfectly sorted
            if nums[l] <= nums[mid]:
                # Is the target within this sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Otherwise, the right half must be perfectly sorted
            else:
                # Is the target within this sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1