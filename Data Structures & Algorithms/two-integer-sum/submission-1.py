class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            # the value we need to add to num to reach to reach target
            complement = target - num 
            if complement in map :
                # return the indices of the two numbners that add up to target
                return [map[complement],i]
            map[num]=i
        