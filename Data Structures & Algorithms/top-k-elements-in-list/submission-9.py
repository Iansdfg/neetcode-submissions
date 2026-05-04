import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_freq = dict()
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1 
        
        heap = []
        for num, freq in num_freq.items():
            heapq.heappush(heap, (-freq, num))
        print(heap)
        res = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res 


        