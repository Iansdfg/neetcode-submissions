class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #buid dic 
        char_cnt = dict()
        for char in s1:
            char_cnt[char] = char_cnt.get(char, 0) + 1 
        
        for pos, char in enumerate(s2):
            temp_dict = char_cnt
            if char in char_cnt:
                if self.check(s1, s2[pos:pos+len(s1)]):
                    return True 
                else:
                    continue 

        return False

    def check(self, s1, s2):
        l1 = [x for x in s1]
        l2 = [x for x in s2]
        print(l1, l2)
        return sorted(l1) == sorted(l2)


        