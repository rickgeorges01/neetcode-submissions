class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creates the HashMap to store the frequency of each num
        num_freq = {}
        for num in nums : 
            if num in num_freq :
                num_freq[num] += 1
            else : 
                num_freq[num] = 1
        s = sorted(num_freq, key = lambda x : num_freq[x], reverse= True )
        return list(s[:k])
        