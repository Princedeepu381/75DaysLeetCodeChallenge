class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # If the first number is positive, the sum can never be 0 (since it's sorted)
            if a > 0:
                break
                
            # Skip duplicate elements for the first position to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Use Two Sum II approach for the remaining elements
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for the left pointer to avoid duplicate triplets
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res