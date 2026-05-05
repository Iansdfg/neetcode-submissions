class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        slow = 0
        for i, interval in enumerate(intervals):
            if i == 0:
                temp = interval
            else:
                if temp[1] >= interval[0]:
                    temp[1] = max(temp[1], interval[1])
                else:
                    intervals[slow] =  temp
                    slow += 1 
                    temp = interval
        intervals[slow] =  temp
        return intervals[:slow+1] 


