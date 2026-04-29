class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_strs = dict()
        for string in strs:
            anagram = self.getAnagram(string)
            if anagram not in anagram_strs:
                anagram_strs[anagram] = []
            anagram_strs[anagram].append(string)
        return list(anagram_strs.values())

    def getAnagram(self, string):
        cnter = [0 for i in range(26)]
        for char in string:
            pos = ord(char) - ord('a')
            cnter[pos] += 1 
        # res = [str(x) for x in cnter]
        print(tuple(cnter))
        return tuple(cnter)

        