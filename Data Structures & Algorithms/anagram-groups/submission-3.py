from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = defaultdict(list)
        for word in  strs:
            wordAnagram = Solution.getAnagrams(word)
            word_group[wordAnagram].append(word) 
        
        res = list(word_group.values())
        return res

    @staticmethod        
    def getAnagrams(word:str)-> tuple:
        counts = [0]*26
        for c in word.lower():
            counts[ord(c) - ord('a')] += 1  
        return tuple(counts)
        