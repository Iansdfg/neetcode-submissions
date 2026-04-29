class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hash_set = set(nums)
        start_cnt = dict()
        for num in nums:
            if num - 1 not in hash_set:
                start_cnt[num] = 1 
        # print(start_cnt)
        visited = set()
        for num in nums:
            if num in start_cnt:
                continue 
            cnt = 0
            target = num - 1
            if target in visited:
                continue 
            if target in hash_set:
                while target in hash_set:
                    cnt += 1 
                    target -= 1 
                    visited.add(target)
                start_cnt[target + 1] = cnt + 1 
        # print(start_cnt)
    
        return max(start_cnt.values())

        