class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_words = dict()

        for word in strs:
            ana = self.get_ana(word)
            if ana not in ana_words:
                ana_words[ana] = []
            ana_words[ana].append(word)
        
        res = []
        for key,val in ana_words.items():
            res.append(val)
        return res 

    def get_ana(self, word):
        return ''.join(sorted(word))
        