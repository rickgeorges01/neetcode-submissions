class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Creates the HashMap to store the frequency of each character
        char_frequency = {}
        # Early condition for a fail fast 
        if len(s) != len(t):
            return False
        for char in s: # O(n)
            if char in char_frequency : 
                char_frequency[char] += 1
            else : 
                char_frequency[char] = 1
        for char in t : # O(n)
            if char in char_frequency : 
                char_frequency[char] -= 1
        # Check if all values in the HashMap are equal to 0
        if all(value == 0 for value in char_frequency.values()) : # O(n)
            return True 
        return False 