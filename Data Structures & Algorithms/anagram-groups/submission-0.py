class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = dict()
        for word in  strs:
            wordAnagram = self.getAnagrams(word)
            if wordAnagram in word_group:
                word_group[wordAnagram].append(word)
            else:
                word_group[wordAnagram] = [word]
        
        res = []
        for key in word_group:
            res.append(word_group[key])
        return res
            


    def getAnagrams(self, word:str)-> str:
        anagram = word.lower()
        print(anagram)
        anagram = sorted(anagram)
        anagram = "".join(anagram)
        return anagram
        