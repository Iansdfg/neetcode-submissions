class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        
        for i in range(len(intervals)):
            if not res or intervals[i][0] > pre_end:
                res.append(intervals[i])
                pre_end = intervals[i][1]
            
            if intervals[i][0] <= pre_end:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
                pre_end = res[-1][1]
        return res 
            
            
