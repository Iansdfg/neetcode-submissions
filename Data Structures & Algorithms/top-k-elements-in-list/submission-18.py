import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ele_cnt = dict()

        for num in nums:
            ele_cnt[num] = ele_cnt.get(num, 0) + 1

        heap = []
        for ele, cnt in ele_cnt.items():
            heapq.heappush(heap, [cnt, ele])
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

        
        