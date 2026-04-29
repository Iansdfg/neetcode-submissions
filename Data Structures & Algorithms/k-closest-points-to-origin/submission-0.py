
import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mini_q = []
        for point in points:
            heapq.heappush(mini_q, (self.getDistance(point), point))
        
        res = []
        for _ in range(k):
            curr = heapq.heappop(mini_q)
            res.append(curr[1])
        return res

    def getDistance(self,point):
        return math.sqrt((point[0])**2 + (point[1])**2)
        