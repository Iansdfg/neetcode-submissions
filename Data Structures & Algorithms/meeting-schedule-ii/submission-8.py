"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x: x.start)
        heap = []
        res = 0
        for interval in intervals:
            heapq.heappush(heap, interval.end)
            if heap[0] <= interval.start:
                heapq.heappop(heap)
            print(heap)
            res = max(res, len(heap))
        return res 
            

        
