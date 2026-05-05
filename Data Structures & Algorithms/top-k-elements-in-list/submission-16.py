import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_freq = dict()
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1 
        
        bucket = [[] for i in range(len(nums)+1)]

        for num, freq in num_freq.items():
            bucket[freq].append(num)

        print(bucket)
        res = []
        for i in range(len(nums), -1, -1):
            if not bucket[i]:
                continue
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                break
        return res 
        
