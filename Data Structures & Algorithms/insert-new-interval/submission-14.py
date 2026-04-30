class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval = [
                    min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        res.append(newInterval)
        return res 
                


        