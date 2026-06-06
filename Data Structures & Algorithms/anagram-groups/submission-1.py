class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create HashMap to store the list of words 
        anagrams_list ={}
        for str in strs : 
            char_list = sorted(str)
            # Convert a list of char in string cause HashMap must be Hashable in Python
            s = ''.join(char_list)
            # what the setdefault does 
            if s in anagrams_list :
                anagrams_list[s].append(str)
            else : 
                anagrams_list[s] = [str]
        return list(anagrams_list.values())