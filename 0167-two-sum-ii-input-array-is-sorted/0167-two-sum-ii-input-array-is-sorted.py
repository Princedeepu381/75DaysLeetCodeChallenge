class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]