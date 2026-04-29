class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        interval_index = 0
        res = []
        while interval_index < len(intervals) and intervals[interval_index][1] < newInterval[0]:
                res.append(intervals[interval_index])
                interval_index += 1 
            
            
        while interval_index < len(intervals) and intervals[interval_index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[interval_index][0])
            newInterval[1] = max(newInterval[1], intervals[interval_index][1])
            interval_index += 1 

        res.append(newInterval)

        while interval_index < len(intervals):
            res.append(intervals[interval_index])
            interval_index += 1

        return res 

            
        