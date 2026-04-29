"""
case1 
newInterval[1] < interval[0]

case2
newInterval[0] > interval[1]

cas3 overlap
else 
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        index = 0
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1 

        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1 
        res.append(newInterval)

        while index < len(intervals) and newInterval[1] < intervals[index][0]:
            res.append(intervals[index])
            index += 1 

        return res 

        