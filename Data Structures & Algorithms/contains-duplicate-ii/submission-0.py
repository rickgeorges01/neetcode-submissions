from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Creates a HashMap to store elements from the array
        seen_nums = {}
        for i,num in enumerate(nums): 
            # Duplicate found, returns immediately
            if num in seen_nums :
                # check the distance between the store index and the current index of the num
                if abs(seen_nums[num]-i) <= k:
                    return True
            seen_nums[num]=i 
        return False 