class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        temp = intervals[0]
        for i, interval in enumerate(intervals):  
            if temp[1] >= interval[0]:
                temp = [min(temp[0], interval[0]), max(temp[1], interval[1])]
            else:
                res.append(temp)
                temp = interval
        
        res.append(temp)
        return res
