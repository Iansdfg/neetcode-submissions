from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = defaultdict(list)
        for word in  strs:
            wordAnagram = self.getAnagrams(word)
            word_group[wordAnagram].append(word) 
        
        res = []
        for key in word_group:
            res.append(word_group[key])
        return res
            


    def getAnagrams(self, word:str)-> str:
        anagram = tuple(sorted(word.lower()))
        return anagram
        