class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = dict()
        for char in s:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1 
        for char in t:
            if char not in char_freq:
                return False
            if char in char_freq:
                char_freq[char] -= 1 
                if char_freq[char] == 0:
                    del char_freq[char] 
        return char_freq == {}

        