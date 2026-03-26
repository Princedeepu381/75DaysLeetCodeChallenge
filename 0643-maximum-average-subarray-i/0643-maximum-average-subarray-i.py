class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        # Slide the window through the rest of the array
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum / k