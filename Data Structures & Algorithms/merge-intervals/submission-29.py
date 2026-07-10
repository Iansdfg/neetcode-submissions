class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        last = intervals[0]
        slow = 0
        for fast, interval in enumerate(intervals):
            if fast == 0:
                continue 
            
            if last[1]>=interval[0]:
                last = [min(last[0],interval[0]), max(last[1],interval[1])]
                
            else:
                intervals[slow] = last
                slow += 1 
                last = interval
        intervals[slow] = last
        return intervals[:slow+1]

            
        