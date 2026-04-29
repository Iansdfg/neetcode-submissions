import heapq
from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1 
        
        min_heap = []

        for num,freq in num_freq.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k: 
                heapq.heappop(min_heap)

        res = []
        while min_heap:
            target = heapq.heappop(min_heap)
            res.append(target[1])

        return res

        