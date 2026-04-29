import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = dict()

        for num in nums:
            num_cnt[num] = num_cnt.get(num, 0) + 1 
        
        heap = []
        for num, cnt in num_cnt.items():
            heapq.heappush(heap, (-cnt, num))

        res = []
        for _ in range(k):
            cnt, num = heapq.heappop(heap)
            res.append(num)
        return res 

        

        


        