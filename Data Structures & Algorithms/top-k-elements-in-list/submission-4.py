from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1 

        items = list(num_freq.items())
        print(items)
    
        items.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(items[i][0])
        return res


