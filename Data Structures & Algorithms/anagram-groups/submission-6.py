from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_strs = defaultdict(list)
        for string in strs:
            ana = self.getAnagram(string)
            ana_strs[ana].append(string)

        return list(ana_strs.values())



    def getAnagram(self, word: str) -> List[int]:
        res = [0 for i in range(26)]
        
        for char in word:
            order = ord(char)-ord('a')
            res[order] += 1
        ana = '.'.join(str(ele) for ele in res)
        return ana

        