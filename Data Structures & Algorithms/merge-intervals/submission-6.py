class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        write = 0 

        for read in range(1, len(intervals)):
            if intervals[read][0] <= intervals[write][1]:
                intervals[write][0] = min(intervals[write][0], intervals[read][0])
                intervals[write][1] = max(intervals[write][1], intervals[read][1])
            else:
                write += 1 
                intervals[write] = intervals[read]
        return intervals[:write+1]

        