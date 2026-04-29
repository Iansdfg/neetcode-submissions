class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for index in range(1, len(intervals)):
            if intervals[index][0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], intervals[index][0])
                res[-1][1] = max(res[-1][1], intervals[index][1])
            elif intervals[index][0] > res[-1][0]:
                res.append(intervals[index]) 
        return res 
        