class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        last = intervals[0]
        
        for index, interval in enumerate(intervals):
            if index == 0:
                continue 
            
            if last[1]>=interval[0]:
                last = [min(last[0],interval[0]), max(last[1],interval[1])]
            else:
                res.append(last)
                last = interval
    

        res.append(last)
        return res

            
        