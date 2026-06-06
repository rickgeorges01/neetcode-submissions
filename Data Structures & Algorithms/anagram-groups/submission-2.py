class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create HashMap to store the list of words 
        anagrams_list ={}
        for str in strs : 
            char_list = sorted(str)
            # Convert a list of char in string cause HashMap must be Hashable in Python
            s = ''.join(char_list)
            # if key doesn't exists initializes  it with a empty list then append 
            anagrams_list.setdefault(s, []).append(str)
        return list(anagrams_list.values())