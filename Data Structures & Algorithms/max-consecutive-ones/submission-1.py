class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones,current = 0,0
        for index in range(len(nums)): 
            if nums[index] == 1: 
                current = current + 1
                max_ones = max(max_ones, current)
            else:
                current = 0
        return max_ones 